var $login = $("input[name='username']")
var $paw = $("input[name='pwd']")
$login.blur(function(){
    var str=$(this).val()
    // var ret=/^[a-zA-Z][a-zA-Z0-9_]{5,20}$/;
    var ret=/^[0-9a-zA-Z\u4e00-\u9fa5_]{3,16}$/;
    if(!ret.test(str)){
        $(this).focus().next().css({display:'block'})
    }
    else{
         $(this).next().html('Username:√').css({"color":"green"})
    }

})
$paw.blur(function(){
    var str=$(this).val()
    var ret=/^[a-zA-Z][a-zA-Z0-9_]{5,20}$/;
    if(!ret.test(str)){
        $(this).focus().next().css({display:'block'})
    }
    else{
         $(this).next().html('password:√').css({"color":"green"})
    }

})