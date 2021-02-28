button = document.getElementById('getProducts')

button.addEventListener('click', async () => {
    const inputBox = document.getElementById('productInput').value
    const table = document.getElementById('myProducts')
    try {
        table.innerHTML = `<div class="d-flex justify-content-center">
                <div class="spinner-border my-5" style="width: 3rem; height: 3rem;" role="status">
                <span class="sr-only">Loading...</span>
            </div>
        </div>`
        const params = {
            method: 'post',
            headers: {
                "Content-type": "text/html; charset=utf-8"
            },
            body: inputBox
        }
        let response = await fetch('http://127.0.0.1:5000/products', params);
        let data = await response.json();
        table.innerHTML = data
        let values = ''
        data.forEach(function (element, index) {
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
    }
    catch {
        table.innerHTML = `<div class="d-flex justify-content-center">
        <span>Something went wrong</span>
            </div>
        </div>`
    }
})