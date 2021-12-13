'use strict';

window.onload = function() {
    console.log('DOM ready');
    $('.table_row').on('change', "input[type='number']", function (event) {
        let quantity = event.target.value;
        let basketItemPk = event.target.name;
        console.log(basketItemPk, quantity);

        $.ajax({
            url: "/basket/update/" + basketItemPk + "/" + quantity + "/",

            success: function (data) {
//            console.log(data);
                if (data.status) {
                    $('.basket_summary').html(data.basket_summary);
                }
            },
        });
       // send to backend
       // get from backend
       // do smth in DOM
    });
}