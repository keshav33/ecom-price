button = document.getElementById('getProducts')

button.addEventListener('click', ()=>{
    inputBox = document.getElementById('productInput').value

    params = {
        method: 'post',
        headers: {
            "Content-type": "text/html; charset=utf-8"
        },
        body: inputBox
    }
    fetch('http://127.0.0.1:5000/name',params).then((response)=>response.json())
    .then((text)=>{
       console.log(text)
    })
    .catch(error=>{
    })

    var loading = true;
    table = document.getElementById('myProducts')

    async function fetchText(){
        let response = await fetch('http://127.0.0.1:5000/products');
        let data = await response.json();
        console.log(data);
        table.innerHTML = data
        let values = ''
        data.forEach(function(element, index){
            console.log(element)
            let value = `
            <tr>
                <td>${element.companyName}</td>
                <td>${element.productName}</td>
                <td>${element.productPrice}</td>
                <td><button type="button" class="btn btn-success" onclick="window.location.href='${element.productLink}';">Click here to buy</button></td>
            </tr>`
            values += value;
        })
        table.innerHTML = `<thead>
        <tr>
            <th scope="col">Provider</th>
            <th scope="col">Product Name</th>
            <th scope="col">Product Price</th>
            <th scope="col">Product Link</th>
        </tr>
    </thead>` + `<tbody>` + values + `</tbody>`
        loading = false;
    }
    fetchText();

    if(loading){
        table.innerHTML = `<div class="d-flex justify-content-center">
        <div class="spinner-border my-5" style="width: 3rem; height: 3rem;" role="status">
          <span class="sr-only">Loading...</span>
        </div>
      </div>`
    }
})