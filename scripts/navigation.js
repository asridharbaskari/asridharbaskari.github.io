(function(){

    var navItems = [
				{href: './pages/index.html', text: 'About'},
				{href: './pages/portfolio.html', text: 'Portfolio'},
				{href: './pages/bookshelf.html', text: 'Bookshelf'},
				{href: './pages/blog.html', text: 'Blog'},
				{href: './pages/resume.html', text: 'Resume'}
		];

    // for (var i = 0; i < navItems.length; i++) {
    //     navItems.href = '../pages/' + navItems.href
    // }

    var test = false; //so my urls don't bugger up in my local environment
    if (!test) {
        for (var i = 0; i < navItems.length; i++) {
            var url = navItems[i].href
            navItems[i].href = 'https://aadithyaa.com/' + url.substring(0, url.length - 5);
        }
    }

    var navElem = document.createElement("nav"),
        navList = document.createElement("ul"), 
        navItem, navLink;

    navElem.appendChild(navList);

    for (var i = 0; i < navItems.length; i++) {
        navItem = document.createElement("li");
        navLink = document.createElement("a");

        navLink.href = navItems[i].href;
        navLink.innerHTML = navItems[i].text;

        navElem.appendChild(navLink);
    }
    window.onload = function () {
        document.body.appendChild(navElem);
    }
}());