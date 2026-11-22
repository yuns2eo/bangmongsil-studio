const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080},deviceScaleFactor:2});
for(const k of ['MONGSIL_Sheet_Felt','MONGSIL_Sheet_Smooth','BANGSIL_Sheet_Felt','BANGSIL_Sheet_Smooth']){await p.goto('file://'+__dirname+'/'+k+'.html');await p.waitForTimeout(500);await p.screenshot({path:__dirname+'/'+k+'.png'});}
await b.close();})();
