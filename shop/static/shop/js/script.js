
// Setting cart object in localstorage


console.log('wel')
cartPro = localStorage.getItem('cartPro')
if (cartPro == undefined) {
    cartObj = {}

}
else {
    cartObj = JSON.parse(localStorage.getItem('cartPro'))
    updateCart(cartObj)
}

// Changing cart value when someone clicked on Add Cart
$('.cartdiv').on('click', 'button.cart', function () {
    console.log(this)

    varID = this.id
    // console.log(varID)
    // console.log(this.id)   // gives id of button which is 
    if (cartObj[varID] != null && cartObj[varID] == 0) {
        qty = cartObj[varID][0]+1

    }
    else {
        qty = 1
        item_name = document.getElementById('name'+varID).innerHTML
        price = parseInt(document.getElementById('price'+varID).innerHTML)
        cartObj[varID] = [qty,item_name,price]
    }
    updateCart(cartObj)

})


// function for updating cart value
function updateCart(cartObj) {

    console.log('updatecart function called')
    console.log(cartObj)
    for (let item in cartObj) {
        document.getElementById('cart' + item).innerHTML = "<button class='btn btn-primary minus' id='minus" + item + "' type='button'>-</button><span id='val" + item + "' class='mx-1'>" + cartObj[item][0] + "</span> <button class='btn btn-primary plus' id='plus" + item + "' type='button'>+</button>"

        for (let item in cartObj) {
            if (cartObj[item][0] == 0)
                document.getElementById('cart' + item).innerHTML = ' <button id="' + item + '" class="btn btn-primary cart">Add To Cart</button>'
        }
    }
    
        localStorage.setItem('cartPro', JSON.stringify(cartObj))
    console.log(cartObj)
    let cartItemNo = document.getElementById('cartItemNo')



    const arr = Object.values(cartObj)
    let total = 0;
    arr.forEach(function (element) {
        total = total + element[0]
    })

    cartItemNo.innerHTML = `<b>${total}</b>`
    updatemodal(cartObj)



}
$('.cartdiv').on('click', 'button.minus', function () {
    key = this.id.slice(5,)
    price = parseInt(document.getElementById('price'+key).innerHTML)

    cartObj[key][0] = cartObj[key][0] - 1
    cartObj[key][2] = cartObj[key][2] - price
    cartObj[key][0] = Math.max(0, cartObj[key][0])
    document.getElementById('val' + key).innerHTML = cartObj[key][0]

    updateCart(cartObj)


})
$('.cartdiv').on('click', 'button.plus', function () {
    key = this.id.slice(4,)
    price = parseInt(document.getElementById('price'+key).innerHTML)

    cartObj[key][0] = cartObj[key][0] + 1
    cartObj[key][2] = cartObj[key][2] + price
    document.getElementById('val' + key).innerHTML = cartObj[key][0]
    updateCart(cartObj)


})

// fucntion for updating the cart modal
function updatemodal(cartObj) {
    console.log("update model called ")
    console.log(cartObj)
    modalStr = ""
    for (let item in cartObj) {
        if(cartObj[item][0]!=0){
            modalStr = modalStr + '<li>' + document.getElementById('name' + item).innerHTML + ' ' + '<b>Qty:</b>' + cartObj[item][0] + '</li>'
        }
    }
    // console.log(modalStr)
    let d = document.getElementById('modalList')
    d.innerHTML = modalStr
    $('#cartmodal').modal('hide')

}
// function for Clearing Cart
$('#clearCart').click(function(){
    console.log('clicked')
    let cart = JSON.parse(localStorage.getItem('cartPro'))
    for(let item in cart){
        document.getElementById('cart'+item).innerHTML='<button id="'+item+'" class="btn btn-primary cart">Add To Cart</button>'
    }
    
    console.log(cartObj)
    localStorage.clear()
    cartObj = {}
    updateCart(cartObj)
})













