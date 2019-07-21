

let request = require('request')
// import request from "request"

let url = 'http://jinwandafiji.club/pw/thread.php?fid=14';
let UserAgents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
    'Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93 Safari/419.3',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13'
]
let user_agent = UserAgents[Math.floor((Math.random() * UserAgents.length))]
let headers = {'User-Agent': user_agent}

/*************
 *
 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)',
 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
 'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
 'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
 'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)',
 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
 'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
 'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
 'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
 *
 * @param url
 **************/

function open_url(url) {

    let opts = {url, headers}
    // console.log(user_agent)
    request(opts, (err, res, body) => {
        if (err) console.error(err)
        find_href(body)
        // console.log(body)
    })
}

function open_imgUrl(url,alldatas,callback) {

    let opts = {url, headers}
    // console.log(user_agent)
    request(opts, (err, res, body) => {
        if (err) console.error(err)
        callback(body,alldatas)
    })
}


function find_href(html){
    // 匹配页面中的链接
    // let b = /<a href =""/gi
    // let b=/<a href=(\"html_data([^<>"\']*)\"|\'([^<>"\']*)\')[^<>]*>/gi;
    let hreflist =[]
    let b = /html_data([^<>"\']*)/gi
    let hrefs =html.match(b)
    hrefs.forEach((e,i)=>{
        if(i%2 ===0){
            let href = "http://k6.csnjcbnxdnb.xyz/pw/" + e
            hreflist.unshift(href)
        }
    })
     // console.log(hreflist)
     find_img(hreflist)
}

function find_img(hreflist){
    let alldatas = []

    console.log(hreflist.length)

    hreflist.forEach( e =>{

        open_imgUrl(e,alldatas,(data,alldatas)=>{

            if(data === null) return
            // 匹配img 的 src 属性
            let b = /http:\/\/p8.urlpic.club\/([^<>"\']*)\.jpg/gi
            let srcs = data.match(b)
            // console.log(srcs)
            if(srcs === null) return
            // 匹配 img 的 title 值
            let t = /\<span id="([^\d\[\]<>"\']*)"\>([^\d\[\]<>"\']*)\[([^<>"\']*)\]\<\/span\>/gi
            let titlelist = data.match(t)
            if(titlelist === null) return
            // console.log(titlelist)
            alldatas.unshift({'title':titlelist[0],'href':srcs,'star':0 ,'collect':false,'delete':false,'download':false})
            console.log(alldatas)
        })
    })

    // Promisefunc()
}

function Promisefunc(){
    return new Promise((resolve,reject)=>{
        find_img(hreflist)
    })
}

// open_imgUrl('http://k6.csnjcbnxdnb.xyz/pw/html_data/14/1907/4194026.html')
open_url(url)

