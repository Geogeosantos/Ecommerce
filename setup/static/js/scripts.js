// Exemplo de produtos no carrinho (dados simulados)
const cartItems = [
    {
        image: '/media/camisa1.png',
        name: 'Produto 1',
        price: 'R$ 99,90'
    },
    {
        image: '/media/camisa2.png',
        name: 'Produto 2',
        price: 'R$ 129,90'
    }
];

// Função para renderizar os itens do carrinho
function renderCart() {
    const cartContainer = document.getElementById("cart-items");
    cartContainer.innerHTML = ""; // Limpa o carrinho antes de adicionar os novos itens

    // Adiciona os itens no carrinho
    cartItems.forEach(item => {
        const div = document.createElement("div");
        div.classList.add("cart-item");

        div.innerHTML = `
            <img src="${item.image}" alt="${item.name}">
            <div class="item-info">
                <p>${item.name}</p>
                <p>${item.price}</p>
            </div>
        `;

        cartContainer.appendChild(div);
    });
}

// Seleciona o botão de fechar e o carrinho
const closeButton = document.querySelector('.close-btn');
const cartContainer = document.querySelector('.cart-container');

// Adiciona o evento de clique no botão de fechar
closeButton.addEventListener('click', function () {
    cartContainer.classList.remove('show'); // Remove a classe 'show' que exibe o carrinho
});

// Seleciona o botão de finalizar compra
const checkoutButton = document.querySelector('.checkout-btn');

// Adiciona um evento de clique ao botão
checkoutButton.addEventListener('click', function () {
    // Aqui você pode redirecionar para uma página de checkout, por exemplo:
    window.location.href = "checkout.html"; // Substitua pela sua página de checkout
});


// Abrir/Fechar o carrinho de compras
document.getElementById("cart-icon").addEventListener("click", function () {
    document.getElementById("cart-container").classList.add("show"); // Exibe o carrinho
    renderCart(); // Renderiza o carrinho quando ele é aberto
});

// Fechar o carrinho de compras
document.getElementById("close-cart").addEventListener("click", function () {
    document.getElementById("cart-container").classList.remove("show"); // Oculta o carrinho
});

function changeLayout(layout) {
    const container = document.querySelector('.grid-produtos');
    
    if (layout === 'list') {
        container.style.gridTemplateColumns = '1fr'; // Exibe os itens em uma coluna (lista)
    } else if (layout === 'grid-4') {
        container.style.gridTemplateColumns = 'repeat(4, 1fr)'; // Exibe 5 itens por linha
    } else if (layout === 'grid-6') {
        container.style.gridTemplateColumns = 'repeat(6, 1fr)'; // Exibe 6 itens por linha
    }
}