import re
def buildID(id):
    s=""
    for i in range(9):
        if i>0:
            s+="-"
        s+=id[7*i:7*i+7]
    return s

s="""
<!DOCTYPE html>
<html  lang="zh">
<meta charset="UTF-8">
<script src="./js/my.js"></script>
<script src="./js/client.js"></script>
<script  type="text/javascript">
        function load(){
            var x;
                var flg=1;
                if (flg)
                {
                        x=window.parent.document.getElementById("RetActivateCID");        
                        if (x) x.value="303010244412085824047884128091547251926122376243";
                        if(true==GetIDParentCheck("btnSelAuto")){
                                SetDlgParent("checkResult","准备自动发送CID.....");
                                window.parent.onSendCID();
                        }
            }else{
                        x=window.parent.document.getElementById("RetActivateCID");
                        if (x) x.value="";
                }
                window.clearTimeout(window.parent.FlgTimer);
                window.parent.FlgTimer=0;
            var x=window.parent.document.getElementById("checkResult");
            if (x) x.innerHTML="此IID正常,成功刷取CID。 :)";

</body>
"""

print(buildID("545490095430251937290276936605004368887324577257053571569708721"))
print(re.search('x.value="(\\d*)"',s)[1])