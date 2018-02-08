/* 
* @Author: anchen
* @Date:   2017-12-07 10:20:56
* @Last Modified by:   anchen
* @Last Modified time: 2017-12-07 10:37:24
*/


window.onload=function(){
    // 左侧导航栏  此处需要完善 2018/01/16
    var oldObj=null;
    // var allLi=document.querySelectorAll('.cont_l>li');
    // for(var i=0;i<allLi.length;i++){
    //     allLi[i].index=i;
    //     allLi[i].click=function(){
    //         console.log(this.index);
    //         this.getElementsByTagName('ul')[0].className="ulBlock";
    //     }
    // }
    $('.cont_l>li').click(function(){

            if(oldObj==this){
                 $(this).find('ul').addClass('ulBlock');
            }else{
                $(this).find('ul').addClass('ulBlock').end().siblings('li').find('ul').removeClass('ulBlock');
            }

    });
    $('.cont_l>li').find('ul').find('li').find('a').click(function(event){
            event.stopPropagation();
    })
};