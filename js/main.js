function test() {
    $('#demo').html("this right");
}

let text = '{ "employees" : [' +
    '{ "firstName":"John" , "lastName":"Doe" },' +
    '{ "firstName":"Anna" , "lastName":"Smith" },' +
    '{ "firstName":"Peter" , "lastName":"Jones" } ]}';



const obj = JSON.parse(text);
console.log(obj);

$(function () {
    $("#demo").html(obj.employees.firstName);
});


$(function () {
    var element = document.getElementById("bmtp");
    var blackprice = Number(element.attributes['value'].value);
    $("#bmtp").html(blackprice)

    var tpic = document.getElementById("tpc");
    var tpicprice = Number(tpic.attributes['value'].value);
    var total = (blackprice + tpicprice);
    console.log(total);
    $("#total").html("總計： " + total)


})
