


document.addEventListener('DOMContentLoaded', function() {
    var botones = document.querySelectorAll('#expand');

    botones.forEach(function(boton) {
        boton.addEventListener('click', function(event) {
            event.preventDefault();

            var imagenDeFondo = window.getComputedStyle(boton.closest('.part-1'), '::before').backgroundImage;
            var urlImagen = imagenDeFondo.slice(5, -2);

            var modal = document.createElement('div');
            modal.classList.add('modal');

            var card = document.createElement('div');
            card.classList.add('card', 'mb-3');
            card.style.maxWidth = '1080px';
            card.style.padding = '20px';
            card.style.zIndex = '800';

            var row = document.createElement('div');
            row.classList.add('row', 'g-0');

            var colImg = document.createElement('div');
            colImg.classList.add('col-md-4');

            var imagen = document.createElement('img');
            imagen.src = urlImagen;
            imagen.classList.add('img-fluid', 'rounded-start');

            var colText = document.createElement('div');
            colText.classList.add('col-md-8');

            var cardBody = document.createElement('div');
            cardBody.classList.add('card-body');
            cardBody.style.display = 'flex';
            cardBody.style.flexDirection = 'column';
            cardBody.style.justifyContent = 'space-between';

            var h5 = document.createElement('h2');
            h5.classList.add('card-title');
            h5.textContent = boton.closest('.single-product').querySelector('.product-title').textContent;
            h5.style.textAlign = 'center';

            var p1 = document.createElement('p');
            p1.classList.add('card-text','mt-3');
            p1.textContent = boton.closest('.single-product').querySelector('.product-text').textContent;

            var priceContainer = document.createElement('div');
            priceContainer.style.display = 'flex';
            priceContainer.style.justifyContent = 'flex-end';

            var p2 = document.createElement('span');
            p2.classList.add('badge', 'rounded-pill', 'product-button', 'mt-2','card-price');
            p2.textContent = boton.closest('.single-product').querySelector('.product-price').textContent;
            p2.style.fontSize = 'xx-large';

            priceContainer.appendChild(p2);

            var p3 = document.createElement('p');
            p3.classList.add('card-brand');
            var small = document.createElement('medium');
            small.classList.add('text-body-secondary');
            small.textContent = boton.closest('.single-product').querySelector('.product-brand').textContent;
            
            var small2 = document.createElement('medium');
            small2.classList.add('text-body-secondary');
            small2.textContent = boton.closest('.single-product').querySelector('.product-stock').textContent;
            
            p3.appendChild(small);

            var closeButtonContainer = document.createElement('div');
            closeButtonContainer.style.position = 'sticky';
            closeButtonContainer.style.top = '0';
            closeButtonContainer.style.right = '0';
            closeButtonContainer.style.textAlign = 'right';

            var closeButton = document.createElement('button');
            var closeIcon = document.createElement('i');
            closeIcon.classList.add('fas', 'fa-times');
            closeButton.appendChild(closeIcon);

            closeButton.textContent = 'X';
            closeButton.style.border = 'Transparent';
            closeButton.style.background = 'Transparent';
            closeButton.addEventListener('click', function() {
                document.body.removeChild(modal);
            });

            closeButtonContainer.appendChild(closeButton);
            card.appendChild(closeButtonContainer);
            
            cardBody.appendChild(h5);
            cardBody.appendChild(p1);
            cardBody.appendChild(p3);
            cardBody.appendChild(small2);
            cardBody.appendChild(priceContainer); // Append the price container instead of p2
            colText.appendChild(cardBody);
            colImg.appendChild(imagen);
            row.appendChild(colImg);
            row.appendChild(colText);
            card.appendChild(row);
            modal.appendChild(card);

            modal.addEventListener('click', function(event) {
                if (event.target === modal) {
                    document.body.removeChild(modal);
                }
            });

            document.body.appendChild(modal);
        });
    });
    
});
if($('.bbb_slider').length)
{
    var trendsSlider = $('.bbb_slider');
    trendsSlider.owlCarousel(
    {
        loop:false,
        margin:30,
        nav:false,
        dots:false,
        autoplayHoverPause:true,
        autoplay:false,
        responsive:
        {
            0:{items:1},
            575:{items:2},
            991:{items:3}
        }
    });

    trendsSlider.on('click', '.bbb_fav', function (ev)
    {
        $(ev.target).toggleClass('active');
    });

    if($('.bbb_prev').length)
    {
        var prev = $('.bbb_prev');
        prev.on('click', function()
        {
            trendsSlider.trigger('prev.owl.carousel');
        });
    }

    if($('.bbb_next').length)
    {
        var next = $('.bbb_next');
        next.on('click', function()
        {
            trendsSlider.trigger('next.owl.carousel');
        });
    }
}
document.querySelectorAll('.bbb_name a').forEach(function(link) {
    link.addEventListener('click', function(event) {
        event.preventDefault();
        var targetId = this.getAttribute('href');
        var targetElement = document.querySelector(targetId);
        var expandLink = targetElement.querySelector('ul a .fa-expand');
        if (expandLink) {
            window.scrollTo(0, targetElement.offsetTop);
            expandLink.click();
        }
    });
});



$('.owl-carousel').owlCarousel({
    loop: true,
    margin: 20,
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 3
        },
        1080: {
            items: 3
        }
    }
});

$(window).resize(function() {
    if ($(window).width() > 768) {
        $('#divdropdown').addClass('d-flex');
    } else {
        $('#divdropdown').removeClass('d-flex');
    }
}).trigger('resize');

$(window).resize(function() {
    if ($(window).width() <= 768) {
        $('#icontel').addClass('ms-auto text-end');
    } else {
        $('#icontel').removeClass('ms-auto');
    }
}).trigger('resize');


