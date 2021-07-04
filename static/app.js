var root = document.documentElement;
var checkbox = document.getElementById('checkbox');
let darkmode = localStorage.getItem('darkMode');
let curtheme = localStorage.getItem('curTheme');
var nightMode = false;

if(darkmode === 'enabled'){
    root.style.setProperty('--tnav-bg', '#424242');
    root.style.setProperty('--content', '#fff');
    root.style.setProperty('--body-bg', '#333');
    root.style.setProperty('--hover-color','#f2aa4cff');
    root.style.setProperty('--snav-bg', '#424242');
    root.style.setProperty('--tnav-shadow', 'rgba(0,0,0,0.5)');
    nightMode = true;
    localStorage.setItem('darkMode','enabled');
}
checkbox.addEventListener('click',function(){
    darkmode = localStorage.getItem('darkMode');
    if(nightMode == true){
        root.style.setProperty('--tnav-bg', '#fff');
        root.style.setProperty('--content', '#424242');
        root.style.setProperty('--snav-bg', '#fff');
        root.style.setProperty('--body-bg', '#fff');
        root.style.setProperty('--hover-color','#ff4f58ff');
        root.style.setProperty('--tnav-shadow', '#E2E1E1');
        nightMode = false;
        localStorage.setItem('darkMode',null);
        localStorage.setItem('curTheme',null);
    }
    else if(nightMode == false){
        root.style.setProperty('--tnav-bg', '#424242');
        root.style.setProperty('--content', '#fff');
        root.style.setProperty('--body-bg', '#333');
        root.style.setProperty('--snav-bg', '#424242');
        root.style.setProperty('--hover-color','#f2aa4cff');
        root.style.setProperty('--tnav-shadow', 'rgba(0,0,0,0.5)');
        nightMode = true;
        localStorage.setItem('darkMode','enabled');
        localStorage.setItem('curTheme',null);

        
    }
});

if(curtheme === 'Theme1'){
    root.style.setProperty('--tnav-bg', '#AF0404');
    root.style.setProperty('--content', '#fff');
    root.style.setProperty('--snav-bg', '#AF0404');
    root.style.setProperty('--body-bg', '#AF0404');
    root.style.setProperty('--tnav-shadow', '#E2E1E1');
    root.style.setProperty('--hover-color','#2d2926ff');
    localStorage.setItem('curTheme','Theme1');
}
if(curtheme === 'Theme2'){
    root.style.setProperty('--tnav-bg', '#16213E');
    root.style.setProperty('--content', '#fff');
    root.style.setProperty('--snav-bg', '#16213E');
    root.style.setProperty('--body-bg', '#1A1A2E');
    root.style.setProperty('--hover-color','#ffd662ff');
    root.style.setProperty('--tnav-shadow', '#E2E1E1');
    localStorage.setItem('curTheme','Theme2');
}
if(curtheme === 'Theme3'){
    root.style.setProperty('--tnav-bg', '#616F39');
    root.style.setProperty('--content', '#fff');
    root.style.setProperty('--snav-bg', '#82A80E');
    root.style.setProperty('--body-bg', '#000');
    root.style.setProperty('--tnav-shadow', '#E2E1E1');
    root.style.setProperty('--hover-color','lightskyblue');
    localStorage.setItem('curTheme','Theme3');
}
if(curtheme === 'Theme4'){
    root.style.setProperty('--tnav-bg', '#BCDBDF');
    root.style.setProperty('--content', '#000');
    root.style.setProperty('--snav-bg', '#235784');
    root.style.setProperty('--body-bg', '#F7A600');
    root.style.setProperty('--hover-color','white');
    root.style.setProperty('--tnav-shadow', '#E2E1E1');
    localStorage.setItem('curTheme','Theme4');
}
if(curtheme === 'Theme5'){
    root.style.setProperty('--tnav-bg', '#363540');
    root.style.setProperty('--content', '#fff');
    root.style.setProperty('--snav-bg', '#CEAEFD');
    root.style.setProperty('--body-bg', '#EE0E51');
    root.style.setProperty('--hover-color','#f2aa4cff');
    root.style.setProperty('--tnav-shadow', '#E2E1E1');
    localStorage.setItem('curTheme','Theme5');
}
if(curtheme === 'Theme6'){
    root.style.setProperty('--tnav-bg', '#2A363B');
    root.style.setProperty('--content', '#fff');
    root.style.setProperty('--snav-bg', '#EB4A5F');
    root.style.setProperty('--body-bg', '#FECEAB');
    root.style.setProperty('--hover-color','red');
    root.style.setProperty('--tnav-shadow', '#E2E1E1');
    localStorage.setItem('curTheme','Theme6');
}
if(curtheme === 'Theme7'){
    root.style.setProperty('--tnav-bg', '#FF5733');
    root.style.setProperty('--content', '#fff');
    root.style.setProperty('--snav-bg', '#C70039');
    root.style.setProperty('--hover-color','darkgreen');
    root.style.setProperty('--body-bg', '#511845');
    root.style.setProperty('--tnav-shadow', '#E2E1E1');
    localStorage.setItem('curTheme','Theme7');
}
if(curtheme === 'Normal'){
    root.style.setProperty('--tnav-bg', '#fff');
    root.style.setProperty('--content', '#424242');
    root.style.setProperty('--snav-bg', '#fff');
    root.style.setProperty('--body-bg', '#fff');
    root.style.setProperty('--tnav-shadow', '#E2E1E1');
    localStorage.setItem('curTheme','Normal');
}

$(document).ready(function(){
    let curtheme = localStorage.getItem('curTheme');
    $('.themeReset').click(function(){
        root.style.setProperty('--tnav-bg', '#fff');
        root.style.setProperty('--content', '#424242');
        root.style.setProperty('--snav-bg', '#fff');
        root.style.setProperty('--body-bg', '#fff');
        root.style.setProperty('--hover-color','#ff4f58ff');
        root.style.setProperty('--tnav-shadow', '#E2E1E1');
        localStorage.setItem('curTheme','Normal');
    });
})

$(document).ready(function(){
    let curtheme = localStorage.getItem('curTheme');
    $('.theme1').click(function(){
        root.style.setProperty('--tnav-bg', '#AF0404');
        root.style.setProperty('--content', '#fff');
        root.style.setProperty('--snav-bg', '#AF0404');
        root.style.setProperty('--body-bg', '#AF0404');
        root.style.setProperty('--tnav-shadow', '#E2E1E1');
        root.style.setProperty('--hover-color','#2d2926ff');
        localStorage.setItem('curTheme','Theme1');
    });
})

$(document).ready(function(){
    let curtheme = localStorage.getItem('curTheme');
    $('.theme2').click(function(){
        root.style.setProperty('--tnav-bg', '#16213E');
        root.style.setProperty('--content', '#fff');
        root.style.setProperty('--snav-bg', '#16213E');
        root.style.setProperty('--body-bg', '#1A1A2E');
        root.style.setProperty('--tnav-shadow', '#E2E1E1');
        root.style.setProperty('--hover-color','#ffd662ff');
        localStorage.setItem('curTheme','Theme2');
    });
})

$(document).ready(function(){
    let curtheme = localStorage.getItem('curTheme');
    $('.theme3').click(function(){
        root.style.setProperty('--tnav-bg', '#616F39');
        root.style.setProperty('--content', '#fff');
        root.style.setProperty('--snav-bg', '#82A80E');
        root.style.setProperty('--body-bg', '#000');
        root.style.setProperty('--hover-color','lightskyblue');
        root.style.setProperty('--tnav-shadow', '#009196');
        localStorage.setItem('curTheme','Theme3');
    });
})

$(document).ready(function(){
    let curtheme = localStorage.getItem('curTheme');
    $('.theme4').click(function(){
        root.style.setProperty('--tnav-bg', '#BCDBDF');
        root.style.setProperty('--content', '#000');
        root.style.setProperty('--snav-bg', '#235784');
        root.style.setProperty('--body-bg', '#F7A600');
        root.style.setProperty('--tnav-shadow', '#E2E1E1');
        root.style.setProperty('--hover-color','white');
        localStorage.setItem('curTheme','Theme4');
    });
})

$(document).ready(function(){
    let curtheme = localStorage.getItem('curTheme');
    $('.theme5').click(function(){
        root.style.setProperty('--tnav-bg', '#363540');
        root.style.setProperty('--content', '#fff');
        root.style.setProperty('--snav-bg', '#CEAEFD');
        root.style.setProperty('--hover-color','#f2aa4cff');
        root.style.setProperty('--body-bg', '#EE0E51');
        root.style.setProperty('--tnav-shadow', '#E2E1E1');
        localStorage.setItem('curTheme','Theme5');
    });
})
$(document).ready(function(){
    let curtheme = localStorage.getItem('curTheme');
    $('.theme6').click(function(){
        root.style.setProperty('--tnav-bg', '#2A363B');
        root.style.setProperty('--content', '#fff');
        root.style.setProperty('--snav-bg', '#EB4A5F');
        root.style.setProperty('--hover-color','red');
        root.style.setProperty('--body-bg', '#FECEAB');
        root.style.setProperty('--tnav-shadow', '#E2E1E1');
        localStorage.setItem('curTheme','Theme6');
    });
});
$(document).ready(function(){
    let curtheme = localStorage.getItem('curTheme');
    $('.theme7').click(function(){
        root.style.setProperty('--tnav-bg', '#FF5733');
        root.style.setProperty('--content', '#fff');
        root.style.setProperty('--snav-bg', '#C70039');
        root.style.setProperty('--body-bg', '#511845');
        root.style.setProperty('--hover-color','darkgreen');
        root.style.setProperty('--tnav-shadow', '#E2E1E1');
        localStorage.setItem('curTheme','Theme7');
    });
})



var snavToggler = document.getElementById('sidenav-toggler');
var isSnav = false;
var snav = document.querySelector('.snavebar');
snavToggler.addEventListener('click',function(){
    if(isSnav == false){
        snav.style.left = '0%';
        isSnav=true;
    }
    else{
        snav.style.left = '-100%';
        isSnav = false;
    }
});

var addToPlaylistBtn = document.querySelector('.addToPlaylistBtn');
var allPlaylists = document.querySelector('.allPlaylists');
var playlistbgOverlay = document.querySelector('.playlistbgOverlay');
var closePlaylist = document.querySelector('.closePlaylist');

var mySwiper = new Swiper('.swiper-container', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
    slidesPerView: 2,
    initialSlide: 0,
    autoplay:true,  
    speed: 300,
    effect: 'slide',
    // spaceBetween: 30,
    // Navigation arrows
    
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    keyboard: {
        enabled: true,
      },
  });

$(document).ready(function(){
    $('.playlistPoster img').click(function(){
        $('.displayPlaylistsLeft img').attr('src',this.src)
    });
})

$(document).ready(function(){
    $('.commentReplyBtn').click(function(){
        // alert('Yo')
        $(this).parent().next('.showReplies').fadeToggle()
    });
});

$(document).ready(function(){
    $('.addToPlaylistBtn').click(function(){
        $('.playlistbgOverlay').show(),
        $('.allPlaylists').show()
        // alert("Yo")
    });
    $('.closePlaylist').click(function(){
        $('.playlistbgOverlay').hide(),
        $('.allPlaylists').hide()
    });
});

Responsive();   

$( window ).resize(function(){
    Responsive();
});   


function Responsive(){
    if($( window ).width() < 950){
        $(document).ready(function(){
            $(".videosActions").attr("id", "newId").appendTo(".videoSingleMid");
        }); 
    } 
    else{
        $(document).ready(function(){
            $(".videosActions").attr("id", "newId").appendTo(".videoSingleTop");
        }); 
    }   
}







