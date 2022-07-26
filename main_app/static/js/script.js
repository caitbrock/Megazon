$('.addToCartBtn').click(function (e) {
    e.preventDefault();

    var product_id = $(this).closest('.product_data')('.product_id').val();
    var product_qty = $(this).closest('.product_data')('.qty-input').val();
    var token = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
        method: 'POST',
        url: '/cart/',
        data: {
            'product_id': product_id,
            'product_qty': product_qty,
            csrfmiddlewaretoken: token
        },
        dataType: 'dataType',
        success: function (response){

        }
    })

});