!function(e){var t={};function o(n){if(t[n])return t[n].exports;var r=t[n]={i:n,l:!1,exports:{}};return e[n].call(r.exports,r,r.exports,o),r.l=!0,r.exports}o.m=e,o.c=t,o.d=function(e,t,n){o.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},o.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.t=function(e,t){if(1&t&&(e=o(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(o.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)o.d(n,r,function(t){return e[t]}.bind(null,r));return n},o.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return o.d(t,"a",t),t},o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},o.p="",o(o.s=0)}([function(e,t,o){o(1),e.exports=o(2)},function(e,t,o){},function(e,t){const o=/(?:^\?|&)([A-z0-9-]+)(?:=([^&]+)|(?=&)|$|=)/g;function n(){const e=function(e){let t=e;if(t||(t=location.search),t.length<2)return null;let n,r={};for(;n=o.exec(t);)r[n[1]]=!n[2]||decodeURIComponent(n[2].replace(/\+/g,"%20"));return r}();null!=e?e.resourcepacks?r("resourcepacks",!1):e.other?r("other",!1):e.pack?loadPack("pack",e.pack,null,!1):e.maps?r("maps",!1):e.map?loadPack("map",e.map,null,!1):e.dungeons?r("dungeons",!1):e.dungeon?loadPack("dungeon",e.dungeon,null,!1):(r("home",!1),history.replaceState(null,"","/")):(r("home",!1),history.replaceState(null,"","/"))}function r(e,t=!0){document.title="Ewan Howell";for(let e of document.querySelectorAll("link[rel='icon']"))e.href=e.dataset.href;t&&("home"==e?history.pushState(null,"","/"):history.pushState(null,"",`?${e}`)),gtag("config","UA-155158328-2",{page_title:e,page_path:location.pathname+location.search});for(let e of document.querySelectorAll(".page"))e.classList.add("hidden");for(let e of document.querySelectorAll(".bannerButton.selected"))e.classList.remove("selected");document.querySelector(`#${e}`).classList.remove("hidden");const o=document.querySelector(`#${e}Button`);null!=o&&o.classList.add("selected"),window.scrollTo(0,0)}window.loadPack=function(e,t,o,n=!0){o&&o.preventDefault(),r(e,!1),n&&history.pushState(null,"",`?${e}=${t}`);for(let e of document.querySelectorAll(".subpage"))e.classList.add("hidden");const l=document.querySelector(`#${t}`);if(null!=l){gtag("config","UA-155158328-2",{page_title:location.search,page_path:location.pathname+location.search}),l.classList.remove("hidden"),document.title=l.dataset.displayName;for(let e of document.querySelectorAll("link[rel='icon']"))e.href=l.dataset.favicon;window.scrollTo(0,0)}else"pack"==e?(r("resourcepacks",!1),history.replaceState(null,"","?resourcepacks")):"map"==e?(r("maps",!1),history.replaceState(null,"","?maps")):"dungeon"==e&&(r("dungeons",!1),history.replaceState(null,"","?dungeons"))},n(),window.addEventListener("popstate",n);for(let e of document.querySelectorAll('[href="/"]'))e.addEventListener("click",(e=>{e.preventDefault(),r("home")}));window.tabClickHandler=function(e){for(let t of e.currentTarget.parentNode.childNodes)t.classList.remove("selected");e.currentTarget.classList.add("selected");const t=e.currentTarget.dataset.tabType,o=e.currentTarget.parentNode.nextSibling;for(let e of o.childNodes)e.classList.add("hidden");o.querySelector(`.${t}`).classList.remove("hidden")},document.querySelector("#resourcepacksButton").addEventListener("click",(e=>{e.preventDefault(),r("resourcepacks")})),document.querySelector("#mapsButton").addEventListener("click",(e=>{e.preventDefault(),r("maps")})),document.querySelector("#dungeonsButton").addEventListener("click",(e=>{e.preventDefault(),r("dungeons")}));for(const e of document.querySelectorAll("img,iframe"))imageObserver.observe(e);document.body.addEventListener("touchend",(e=>{if(e.currentTarget.classList.contains("bannerDrop"))for(const t of document.querySelectorAll(".menu.touch-open"))t!=e.currentTarget.querySelector(".menu")&&t.classList.remove("touch-open");else for(const e of document.querySelectorAll(".menu.touch-open"))e.classList.remove("touch-open")}));const l=e=>{e.currentTarget.querySelector(".menu").classList.add("touch-open")};for(const e of document.querySelectorAll(".bannerDrop"))e.addEventListener("touchend",l)}]);