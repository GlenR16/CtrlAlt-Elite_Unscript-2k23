$(".buttons").click(function(event){
    if (Cookies.get("clicked") === undefined){
        tempcookie = "";
    }
    else{
        tempcookie = Cookies.get("clicked") + ",";
    }
    Cookies.set("clicked", tempcookie +event.target.id);
});