const rgxURLParams = /(?:^\?|&)([A-z0-9-]+)(?:=([^&]+)|(?=&)|$|=)/g

function getURLParams(s) {
	let str = s
	if (!str) str = location.search
	if (str.length < 2) return null
	let params = {}
	let m; while (m = rgxURLParams.exec(str)) {
		params[m[1]] = m[2] ? decodeURIComponent(m[2].replace(/\+/g, "%20")) : true
	}
	return params
}

function toURLParams(o) {
	let arr = []
	for (let k in o) if (o.hasOwnProperty(k) && o[k] != null) {
		if (o[k] === true) {
			arr.push(`${arr.length == 0 ? "?" : "&"}${k}`)
		} else {
			let encodedVal = encodeURIComponent(o[k])
				.replace(/%3A/g, ':')
				.replace(/%3B/g, ';')
				.replace(/%20/g, '+')
				.replace(/%2C/g, ',')
				.replace(/%2F/g, '/')
				.replace(/%40/g, '@')
			arr.push(`${arr.length == 0 ? "?" : "&"}${k}=${encodedVal}`)
		}
	}
	return arr.join("")
}

function pageLoad(){
	const params = getURLParams()
	if (params != null){
		if (params.resourcepacks) {
			showPage("resourcepacks", false)
		} else if (params.other) {
			showPage("other", false)
		} else if (params.pack) {
			loadPack("pack", params.pack, null, false)
		} else if (params.maps) {
			showPage("maps", false)
		} else if (params.map) {
			loadPack("map", params.map, null, false)
		} else if (params.dungeons) {
			showPage("dungeons", false)
		} else if (params.dungeon) {
			loadPack("dungeon", params.dungeon, null, false)
		} else if (params.renders) {
			showPage("renders", false)
		} else {
			showPage("home", false)
			history.replaceState(null, "", "/")
		}
	} else {
		showPage("home", false)
		history.replaceState(null, "", "/")
	}
}

window.loadPack = function(type, pack, evt, updateState = true){
	if (evt){
		evt.preventDefault()
	}
	showPage(type, false)
	if (updateState){
		history.pushState(null, "", `?${type}=${pack}`)
	}
	for (let page of document.querySelectorAll(".subpage")){
		page.classList.add("hidden")
	}
	const packData = document.querySelector(`#${pack}`)
	if (packData == null){
		if(type == "pack"){
			showPage("resourcepacks", false)
			history.replaceState(null, "", "?resourcepacks")
		}else if (type == "map"){
			showPage("maps", false)
			history.replaceState(null, "", "?maps")
		}else if (type == "dungeon"){
			showPage("dungeons", false)
			history.replaceState(null, "", "?dungeons")
		}
		return
	}
	gtag("config", "UA-155158328-2", {
		"page_title" : location.search,
		"page_path": location.pathname+location.search
	})
	packData.classList.remove("hidden")
	document.title = packData.dataset.displayName
	for (let icon of document.querySelectorAll("link[rel='icon']")){
		icon.href = packData.dataset.favicon
	}
	window.scrollTo(0, 0)
}

function showPage(pageName, updateState = true){
	document.title = "Ewan Howell"
	for (let icon of document.querySelectorAll("link[rel='icon']")){
		icon.href = icon.dataset.href
	}
	if (updateState){
		if (pageName == "home"){
			history.pushState(null, "", "/")
		} else {
			history.pushState(null, "", `?${pageName}`)
		}
	}
	gtag("config", "UA-155158328-2", {
		"page_title" : pageName,
		"page_path": location.pathname+location.search
	})
	for (let page of document.querySelectorAll(".page")){
		page.classList.add("hidden")
	}
	for (let button of document.querySelectorAll(".bannerButton.selected")){
		button.classList.remove("selected")
	}
	document.querySelector(`#${pageName}`).classList.remove("hidden")
	const pageButton = document.querySelector(`#${pageName}Button`)
	if (pageButton != null){
		pageButton.classList.add("selected")
	}
	window.scrollTo(0, 0)
}

pageLoad()

window.addEventListener("popstate", pageLoad)

for (let button of document.querySelectorAll('[href="/"]')){
	button.addEventListener("click", evt => {
		evt.preventDefault()
		showPage("home")
	})
}

window.tabClickHandler = function(evt){
	for (let tabButton of evt.currentTarget.parentNode.childNodes){
		tabButton.classList.remove("selected")
	}
	evt.currentTarget.classList.add("selected")
	const tabName = evt.currentTarget.dataset.tabType
	const tabContainer = evt.currentTarget.parentNode.nextSibling
	for (let tab of tabContainer.childNodes){
		tab.classList.add("hidden")
	}
	tabContainer.querySelector(`.${tabName}`).classList.remove("hidden")
}

document.querySelector("#resourcepacksButton").addEventListener("click", evt => {
	evt.preventDefault()
	showPage("resourcepacks")
})

document.querySelector("#mapsButton").addEventListener("click", evt => {
	evt.preventDefault()
	showPage("maps")
})

document.querySelector("#dungeonsButton").addEventListener("click", evt => {
	evt.preventDefault()
	showPage("dungeons")
})

document.querySelector("#rendersButton").addEventListener("click", evt => {
	evt.preventDefault()
	showPage("renders")
})

for (const el of document.querySelectorAll("img,iframe")) {
	imageObserver.observe(el)
}

document.body.addEventListener("touchend", e => {
	if (e.currentTarget.classList.contains("bannerDrop")) {
		for (const menu of document.querySelectorAll(".menu.touch-open")) {
			if (menu == e.currentTarget.querySelector(".menu")){
				continue
			}
			menu.classList.remove("touch-open")
		}
	} else {
		for (const menu of document.querySelectorAll(".menu.touch-open")) {
			menu.classList.remove("touch-open")
		}
	}
})

const openMenuFunc = e => {
	const menu = e.currentTarget.querySelector(".menu")
	menu.classList.add("touch-open")
}

for (const menuTitle of document.querySelectorAll(".bannerDrop")) {
	menuTitle.addEventListener("touchend", openMenuFunc)
}

window.processSearch = function(evt){
	for (const card of document.querySelectorAll("#resourcepacks .pack")){
		const searchList = card.dataset.search.split(";")
		card.classList.add("hidden")
		for (const item of searchList){
			if (~item.toLowerCase().indexOf(evt.currentTarget.value.toLowerCase())){
				card.classList.remove("hidden")
			}
		}
	}
	for (const category of document.querySelectorAll("#resourcepacks h2+.container")){
		category.classList.add("hidden")
		category.previousSibling.classList.add("hidden")
		if (Array.from(category.children).some(e => !e.classList.contains("hidden"))){
			category.classList.remove("hidden")
			category.previousSibling.classList.remove("hidden")
		}
	}
}

const data = require("../assets/site.json")
const exclusions = [
	"legacy"
]
const allPacks = data.resourcepacks.filter(e => !~exclusions.indexOf(e.category.toLowerCase())).reduce((a, e) => a.concat(e.packs.map(f => {
	f.category = e.category
	return f
})), [])

const packData = allPacks[Math.floor(Math.random()*allPacks.length)]

const img = new Image
img.src = require(`../assets/images/banners/${packData.name}.png`).default

const container = document.createElement("div")
const category = document.createElement("p3")
const title = document.createElement("h2")
const subheading = document.createElement("p2")
const description = document.createElement("p2")

category.textContent = packData.category.toUpperCase()
title.textContent = packData.displayName
subheading.textContent = packData.details.subheading
description.textContent = packData.details.description

container.append(category, title, subheading, document.createElement("br"), document.createElement("br"), description)
container.classList.add("featureContentText")

const featureContent = document.querySelector(".featureContent")

featureContent.append(img, container)
featureContent.addEventListener("click", evt => loadPack("pack", packData.name, evt))