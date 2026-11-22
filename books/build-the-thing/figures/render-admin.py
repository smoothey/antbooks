import asyncio, json, base64, sys, os
from playwright.async_api import async_playwright
JWT='e30.'+base64.urlsafe_b64encode(json.dumps({"exp":4102444800,"email":"admin@example.com","name":"Admin"}).encode()).decode().rstrip('=')+'.sig'
PH=[open(f'/home/claude/adm/ph{i}.jpg','rb').read() for i in range(4)]
def photos():
    out=[]
    for i in range(12):
        out.append({"id":f"p{i}","title":f"Shoot {i+1}","alt":"Placeholder photo","category":["portrait","fashion","studio"][i%3],"categories":[["portrait","fashion","studio"][i%3]],"tags":[],"with":[],"details":{},"galleries":[],"published":True,"width":4000,"height":6000,"photographer":"","status":"ready","order":i,"shoot":f"s{i//4}","url":f"/ph/{i%4}.jpg","thumb":f"/ph/{i%4}.jpg","thumbUrl":f"/ph/{i%4}.jpg","src":f"/ph/{i%4}.jpg"})
    return out
STUB_SI="""(function(){var T='%s';window.PoserollSignIn=new Proxy({current:async()=>T,token:()=>T,clear(){},canPasskey:()=>false,passkeyHere:()=>false,microsoftReturn:async()=>null,onChange(){},render(){},offerPasskey(){},signOut:async()=>{}},{get(t,k){return k in t?t[k]:(()=>null)}});})();"""%JWT
STUB_G="""window.google={accounts:{id:{initialize(o){setTimeout(()=>o.callback({credential:'%s'}),50)},renderButton(){},prompt(){},disableAutoSelect(){}}}};"""%JWT
async def run(date, root, route, out):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1280,'height':800})
        errs=[]
        pg.on('pageerror',lambda e:errs.append(str(e)[:120]))
        async def handler(r):
            u=r.request.url
            path=u.split('://',1)[1].split('/',1)[1] if '/' in u.split('://',1)[1] else ''
            path='/'+path.split('?')[0]
            if False: return await r.fulfill(body=STUB_G,content_type='application/javascript')
            if u.startswith('http://local/'):
                if path=='/config.js': return await r.fulfill(body="window.SITE_CONFIG={googleClientId:'x',apiBase:'/api',mediaBase:''};",content_type='application/javascript')
                if path=='/assets/signin.js': return await r.fulfill(body=STUB_SI,content_type='application/javascript')
                if any(k in path for k in ('logo','badge','favicon','brand')): return await r.fulfill(body='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="#6B6B6B"/><rect x="20" y="20" width="24" height="24" rx="3" fill="none" stroke="#fff" stroke-width="3"/></svg>''',content_type='image/svg+xml')
                if path.startswith('/ph/'): return await r.fulfill(body=PH[int(path[4])],content_type='image/jpeg')
                if path.startswith('/api/'):
                    p2=path[len('/api/'):]
                    if p2.endswith('thumb') or 'thumb' in p2 or 'file' in p2: return await r.fulfill(body=PH[0],content_type='image/jpeg')
                    if p2.endswith('manage/photos') or p2=='manage/photos': body={"photos":photos()}
                    elif 'photographers' in p2: body={"photographers":[]}
                    elif 'collaborators' in p2: body={"collaborators":[]}
                    elif 'me' in p2.split('/')[-1] or 'session' in p2: body={"user":{"email":"admin@example.com","name":"Admin","role":"owner"}}
                    else:
                        L=[]
                        body={k:L for k in ['categories','photos','galleries','items','enquiries','reviews','admins','links','list','uploads','proofs','people','photographers','collaborators','bugs','jobs','events','pages','images','visits','days','rows','results','activity','recent','queue','groups','shoots','tasks','recs','sections']}
                        body.update({"categories":[{"slug":"portrait","name":"Portrait"},{"slug":"fashion","name":"Fashion"},{"slug":"studio","name":"Studio"}],"watermark":{},"counts":{},"total":0,"count":0,"unread":0,"ok":True})
                    return await r.fulfill(body=json.dumps(body),content_type='application/json')
                f=os.path.join(root,path.lstrip('/'))
                if path.endswith('/'): f=os.path.join(f,'index.html')
                if os.path.isdir(f): f=os.path.join(f,'index.html')
                if os.path.exists(f):
                    ct={'js':'application/javascript','css':'text/css','html':'text/html','svg':'image/svg+xml','png':'image/png','webp':'image/webp','json':'application/json'}.get(f.rsplit('.',1)[-1],'application/octet-stream')
                    return await r.fulfill(body=open(f,'rb').read(),content_type=ct)
                return await r.fulfill(status=404,body='')
            if 'accounts.google.com' in u: return await r.fulfill(body='',content_type='application/javascript')
            if 'fonts.g' in u or 'cdnjs' in u: return await r.continue_()
            return await r.abort()
        await pg.route('**/*',handler)
        await pg.add_init_script(STUB_G+"try{sessionStorage.setItem('idToken','%s')}catch(e){}"%JWT)
        await pg.goto(f'http://local/admin/{route}',wait_until='load')
        await pg.wait_for_timeout(3500)
        await pg.screenshot(path=out)
        print(date,'errors:',errs[:4])
        await b.close()
d=sys.argv[1]; asyncio.run(run(d,f'/home/claude/adm/{d}/site',sys.argv[2] if len(sys.argv)>2 else '',f'/home/claude/adm/shots/{d}.png'))
