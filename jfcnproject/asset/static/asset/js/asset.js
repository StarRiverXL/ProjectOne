/* 
* @Author: anchen
* @Date:   2017-12-07 10:20:56
* @Last Modified by:   anchen
* @Last Modified time: 2017-12-07 10:37:24
*/


window.onload=function(){
    // 添加设备
    console.log("adddddddddddddaaaa");
    var aAdd=document.querySelector('.addEqu');
    var canopy=document.querySelector('.canopy');
    var edit=document.querySelectorAll('.edit');
    var reset=document.querySelector('.reset');
    aAdd.onclick=function(){
        console.log("addddddddddddd");
        canopy.style.display='block';
    };
    for(var i=0;i<edit.length;i++){
        edit[i].onclick=function(ev){
            var ev= ev || window.event;
            console.log(ev.target);
            canopy.style.display='block';
        };
    }
    reset.onclick=function(){
        canopy.style.display='none';
    };

};