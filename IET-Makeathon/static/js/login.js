$unarr=new Array("sthit", "kunal", "jinit", "ayush", "vibhor");
$pwdarr=new Array("sthit", "kunal", "jinit", "ayush", "vibhor");

function verify()
{
    $flag=1;
    $un=document.f1.un.value;
    $pwd=document.f1.pwd.value;
    for($i=0;$i<5;$i++)
    {
        if($un==$unarr[$i] && $pwd==$pwdarr[$i])
        {
            alert("Login Successful");
            window.location("./");
            $flag=0;
        }
    }
    if($flag==1)
    {
        alert("Wrong Password");
    }
}
