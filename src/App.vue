<!--suppress ALL -->
<style lang="scss" scoped>
div#app {
  height: auto;
}

/*滚动条样式*/
.el-row::-webkit-scrollbar {
  /*滚动条整体样式*/
  width: 0px;
  /*高宽分别对应横竖滚动条的尺寸*/
  height: 0px;
}

.el-row::-webkit-scrollbar-thumb {
  /*滚动条里面小方块*/
  border-radius: 0px;
  box-shadow: inset 0 0 5px rgba(230, 203, 233, 0.2);
  background: rgba(211, 196, 228, 0.2);
}

.el-row::-webkit-scrollbar-track {
  /*滚动条里面轨道*/
  box-shadow: inset 0 0 5px rgba(223, 206, 235, 0.2);
  border-radius: 0;
  background: rgba(234, 204, 235, 0.1);
}
/*滚动条样式*/
.allpicture::-webkit-scrollbar {
  /*滚动条整体样式*/
  width: 10px;
  /*高宽分别对应横竖滚动条的尺寸*/
  height: 0px;
}
$scrcolor: rgba(226, 189, 191, 0.9);

.allpicture::-webkit-scrollbar-thumb {
  /*滚动条里面小方块*/
  border-radius: 5px;
  box-shadow: inset 0 0 5px rgba(230, 203, 233, 0.2);
  background: $scrcolor;
}

.allpicture::-webkit-scrollbar-track {
  /*滚动条里面轨道*/
  box-shadow: inset 0 0 5px rgba(223, 206, 235, 0.2);
  border-radius: 5px;
  background: rgba(234, 204, 235, 0.1);
}

.boxblur{
  filter: blur(20px)
}

.el-row {
  // display: none;

  background-size: 30px 30px;
  position: fixed;
  overflow: scroll;
  .actpicture {
    justify-content: start !important;
    overflow: scroll;
    div {
      position: relative;
      img {
        cursor: pointer;
        min-height: 230px;
        height: auto !important;
        width: 94% !important;
        &:hover {
          border: solid 1px rgb(0, 162, 255);
        }
      }
      div.iconbox {
        display: none;
      }
    }
  }
  // css 动画效果
  @for $i from 1 through 20 {
    div.bounceInUp:nth-child(#{$i}) {
      animation-delay: ($i * 0.1) + s;
    }
  }
  .zoomIn {
    animation-delay: 0.2s;
  }

  .allpicture {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    max-height: 100vh;
    overflow: scroll;

    div {
      position: relative;
      width: auto;
      height: auto;
      margin: 10px;
      z-index: 10;
      $allimgH: 230px;
      $allimgW: auto;
      i.showcollect {
        position: absolute;
        color: red;
        left: 0px;
        top: 5px;
        transform: rotate(-90deg);
      }
      i.righticon {
        position: absolute;
        opacity: 0.8;
        height: 100%;

        .el-button {
          position: absolute;
          left: -30px;
          top: 5px;
          z-index: 1;
          padding: 0px;
        }
        .ratenode {
          top: 25px;
          left: -40px;
        }
      }
      div.iconbox {
        top: 0;
        position: absolute;
        overflow: hidden;
        width: 100%;
        height: 100%;
        margin: 0 auto;
        &:hover {
          div.top-msg {
            top: 0px;
            // display: block;
          }
          div.bottom-msg {
            bottom: -150px;
            opacity: 1;
          }
        }
        div {
          // display: none;
          width: 100%;
          transition: all 0.4s ease-in-out;
          color: rgb(255, 255, 255);
          font-size: 12px;
          letter-spacing: 2px;
          margin: 0 auto;
        }
        div.top-msg {
          height: 35px;
          top: -35px;
          opacity: 0.7;
          background: linear-gradient(rgb(41, 41, 41), rgba(109, 109, 109, 0));
        }
        div.bottom-msg {
          height: 25px;
          bottom: -210px;
          background: rgba(39, 39, 39, 0);
          opacity: 0;
          text-align: center;
          i {
            font-size: 25px;
            z-index: 99;
          }
        }
      }
      img {
        min-width: 150px;
        height: $allimgH;
        width: $allimgW;
        border: 1px solid rgb(250, 244, 244);
        box-shadow: 1px 1px 3px 1px rgb(134, 129, 129);
      }
    }
  }
  /*滚动条样式*/
  .folderpicture::-webkit-scrollbar {
    /*滚动条整体样式*/
    width: 10px;
    /*高宽分别对应横竖滚动条的尺寸*/
    height: 0px;
  }

  .folderpicture::-webkit-scrollbar-thumb {
    /*滚动条里面小方块*/
    border-radius: 5px;
    box-shadow: inset 0 0 5px rgba(230, 203, 233, 0.2);
    background: $scrcolor;
  }

  .folderpicture::-webkit-scrollbar-track {
    /*滚动条里面轨道*/
    box-shadow: inset 0 0 3px rgba(223, 206, 235, 0.2);
    border-radius: 5px;
    background: rgba(234, 204, 235, 0.1);
  }

  // **************  css random color  ***************
  $color1: rgb(random(255), random(255), random(255));
  $color2: rgb(random(255), random(255), random(255));
  $color3: rgb(random(255), random(255), random(255));
  $color4: rgb(random(255), random(255), random(255));
  $color5: rgb(random(255), random(255), random(255));
  $color6: rgb(random(255), random(255), random(255));
  $color7: rgb(random(255), random(255), random(255));
  $color8: rgb(random(255), random(255), random(255));
  $color9: rgb(random(255), random(255), random(255));
  $color10: rgb(random(255), random(255), random(255));
  $color11: rgb(random(255), random(255), random(255));
  $color12: rgb(random(255), random(255), random(255));
  $color13: rgb(random(255), random(255), random(255));
  $color14: rgb(random(255), random(255), random(255));
  $colorlist: $color1, $color2, $color3, $color4, $color5, $color6, $color7,
    $color8, $color9, $color10, $color10, $color11, $color12, $color13, $color14;
  @mixin bg-color() {
    /*generate a random number between 1 and the length of the list*/
    $random-color: random(length($colorlist));
    /*return an item from the list based on the random number*/
    background: nth($colorlist, $random-color);
  }
  //^^^^^^^^^^^^^^^^^^^^css random color ^^^^^^^^^^^^^^

  .folderpicture {
    max-height: 100vh;
    display: flex;
    justify-content: space-around;
    overflow: scroll;
    flex-wrap: wrap;
    @for $i from 1 through 65 {
      div:nth-child(#{$i}) {
        perspective: 1000px;
        margin: 10px;
        &:hover {
          img {
            transform: rotateY(180deg);
          }
          .back {
            transform: rotateY(0deg);
          }
        }
        &:nth-child(even):hover {
          img {
            transform: rotateY(-180deg);
          }
          .back {
            transform: rotateY(0deg);
          }
        }
        &:nth-child(even) {
          .back {
            transform: rotateY(180deg);
          }
        }
        img {
          border-radius: 6px;
          min-width: 150px;
          height: 230px;
          width: auto;
          cursor: pointer;
          // border: 2px solid rgb(255, 255, 255);
          box-shadow: 1px 1px 3px 1px rgb(150, 148, 148);
          transition: ease-in-out 600ms;
          backface-visibility: hidden;
          border: 1px solid rgb(250, 244, 244);
        }

        .back {
          opacity: 0.95;
          @include bg-color;
          border: 1px solid rgba(250, 244, 244, 0.6);
          // background: white;
          color: rgb(255, 255, 255);
          top: 0px;
          right: 0px;
          left: 0px;
          border-radius: 6px;
          position: absolute;
          transform: rotateY(-180deg);
          height: 230px;
          width: 100%;
          margin: 0;
          backface-visibility: hidden;
          transition: ease-in-out 600ms;
          // box-shadow: 1px 1px 5px rgb(121, 120, 120);
          overflow: hidden;
          p {
            margin: 12px;
          }
          div {
            // position: absolute;
            margin-top: 90px;
            display: flex;
            justify-content: space-around;
            .el-button {
              border: 1px solid rgba(253, 243, 243, 0.4);
              padding: 10px;
              transition: all ease-in-out 0.6s;
              // box-shadow: rgb(85, 85, 85) 0px 0.1px 10px;
              &:hover {
                // box-shadow: rgb(136, 136, 136) 0px 0.3px 8px ;
              }
            }
          }
        }
      }
    }
  }

  .lgbox {
    -webkit-app-region: drag;
    position: absolute;
    width: 100vw;
    height: 100vh;
    z-index: 100;
    text-align: center;
    // background: burlywood;
    // linear-gradient(
    //     rgba(216, 191, 142, 0.4) 50%,
    //     rgba(81, 134, 170, 0.3) 50%
    //   ),
    //   linear-gradient(
    //     90deg,
    //     rgba(253, 184, 47, 0.3) 50%,
    //     rgba(81, 134, 170, 0.4) 50%
    //   );
    background-size: 30px 30px;
    &::before{
      content: '';
      position: absolute;
      top: 0;bottom: 0;left: 0;right: 0;
      filter: blur(20px);
      margin: -30px;
      opacity: 0.2;
      background: $color1 0 / cover fixed;
      z-index: -1;
    }
    $smboxH: 0vh;
    .el-icon-close {
      border-radius: 50%;
      // border:1.2px solid rgb(226, 1, 69);
      box-shadow: 15px 0px 120px rgba(0, 0, 0, 0.4) inset;
      -webkit-app-region: no-drag;
      font-size: 1.6em;
      position: absolute;
      top: 10px;
      right: 10px;
      color: white;
      opacity: 0.6;
      transition: ease-in-out 0.2s;
      // filter: Glow(color = wihte,strength = 255)
    }
    .el-icon-close:hover {
      transform: rotate(90deg);
      opacity: 1;
    }
    .arrowicon {
      -webkit-app-region: no-drag;
      font-size: 10em;
      position: absolute;
      margin-top: 35vh;
      color: rgba(240, 248, 255, 0);
      transition: all 0.8s;
    }
    .arrowicon:hover {
      color: rgba(240, 248, 255, 1);
    }
    .el-icon-arrow-right {
      right: 0;
    }
    .el-icon-video-play {
      left: 46.5%;
      // z-index: 2;
    }
    .el-icon-video-pause {
      left: 46.5%;
      // z-index: 2;
    }
    .el-icon-arrow-left {
      left: 0;
    }
    img {
      -webkit-app-region: no-drag;
      height: 100vh;
      width: auto;
      min-width: 250px;
      box-shadow: 0 0 0px 2px rgb(255, 255, 255);
      transition: all 0.2s;
    }
    div.smbox {
      -webkit-app-region: no-drag;
      // transition: all 0.3s;
      bottom: 0;
      width: 100vw;
      height: $smboxH;
      display: flex;
      justify-content: start;
      overflow: scroll;
    }
  }
  .smallbar {
    div.smbox {
      height: 14vh;
      background: rgba(255, 241, 223, 0.8);
      div {
        margin-left: 0.5em;
        transition: all 0.3s;
        z-index: 99;
        height: 10vh;
        margin-top: 3vh;

        &:hover {
          margin-top: 0.5vh;
        }
      }
      img {
        height: 10vh !important;
        width: auto;
        min-width: 7vh;
      }
    }
    img {
      height: 85vh !important;
    }
  }
}

/*滚动条样式*/
.smbox::-webkit-scrollbar {
  /*滚动条整体样式*/
  width: 0px;
  /*高宽分别对应横竖滚动条的尺寸*/
  height: 0px;
}

.smbox::-webkit-scrollbar-thumb {
  /*滚动条里面小方块*/
  border-radius: 0px;
  box-shadow: inset 0 0 0px rgba(230, 203, 233, 0.2);
  background: $scrcolor;
}

.smbox::-webkit-scrollbar-track {
  /*滚动条里面轨道*/
  box-shadow: inset 0 0 0px rgba(223, 206, 235, 0.2);
  border-radius: 0px;
  background: rgba(234, 204, 235, 0.1);
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>

<template>
  <div id="app">
    <!-- @getcollectfunc="getCollectfunc()"  -->
    <top-bar
      ref="topbar"
      v-show="showtopbarflag"
      @getTopBarfunc="getTopBarFunc"
      @backhomefunc="backhome"
      @getmore="getmore"
    />
    <el-row>
      <el-col :class="{'actpicture':actflag}" class="allpicture" :span="laycont">
        <div ref="imgdoms" class="tImgCard" v-show="!e.delete" v-for="(e,i) in allHrefs" :key="i">
          <img :src="e.href[1]" class="image" @click="showthisFolder(e)" />
          <i v-show="e.collect" class="showcollect el-icon-collection-tag"></i>
          <i class="righticon">
            <el-button size="mini" type="danger" disabled>{{e.href.length}} P</el-button>
            <el-button class="ratenode" size="mini" type="danger" disabled>
              {{e.star}}
              <i class="el-icon-ice-cream"></i>
            </el-button>
          </i>
          <div class="iconbox" @click="showthisFolder(e)">
            <div class="top-msg" v-html="e.title"></div>
            <downloadtool :downtooldata="e" @savefile="saveFile()" />
          </div>
        </div>
      </el-col>
      <el-col class="folderpicture animated zoomIn" :span="24" v-show="folderflag">
        <div  class="imgcard" v-for="(e,i) in hrefs.href" :key="i">
          <img class="front" :src="e" alt @click="showlgpic(e)" />
          <div class="back" @click="showlgpic(e)">
            <p v-html="hrefs.title"></p>
            <div>
              <el-button size="medium" type="danger" round @click.stop.prevent>喜欢</el-button>
              <el-button size="medium" type="warning" round @click.stop.prevent="deletepic(i)">删除</el-button>
            </div>
          </div>
        </div>
      </el-col>
      <transition name="fade">
        <div
          class="lgbox"
          :class="{'smallbar':smallbarflag}"
          v-show="showlgpicflag"
          @mousemove="mousemovefunc($event)"
          ref="smallbar"
        >
          <i class="el-icon-close" @click="closethis()"></i>
          <i
            ref="arrowstop"
            class="arrowicon"
            :class="arrowclassicon[arrowflag]"
            @click="arrowfunc('mid')"
          ></i>
          <i
            class="arrowicon el-icon-arrow-left"
            @click="arrowfunc('left')"
            @keydown.left="arrowfunc('left')"
          ></i>

          <i
            class="arrowicon el-icon-arrow-right"
            @click="arrowfunc('right')"
            @keyup.right="arrowfunc('right')"
          ></i>

          <img class="lgboximg" :src="lghref" @click="maxWindow()" alt />
          <div class="smbox" ref="smbox">
            <div v-for="(e,i) in hrefs.href" :key="i">
              <img :src="e" alt @mouseover="showlgpic(e)" />
            </div>
          </div>
        </div>
      </transition>
    </el-row>
  </div>
</template>

<script>
import TopBar from "./components/TopBar.vue";
import downloadtool from "./components/downloadtool";

let request = require("request");
/*******
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6",
 "Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93 Safari/419.3",
 "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13"
 */
let UserAgents = [
  "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13"
];
let user_agent = UserAgents[Math.floor(Math.random() * UserAgents.length)];
let headers = { "User-Agent": user_agent };

import fs, { promises, constants } from "fs";
import { Promise, timeout } from "q";
let file = "./picturehref.json";

export default {
  name: "sexpicture",
  components: { TopBar, downloadtool },
  props: {
    msg: String
  },
  data() {
    return {
      delhrefs: [],
      allHrefs: [],
      allHrefsTemp: [],

      folderflag: false,
      laycont: null,
      hrefs: [],
      lghref: "",
      currentDate: new Date().toLocaleString(),
      rateValue: null,
      showlgpicflag: false,
      actflag: false,
      smallbarflag: false,
      showtopbarflag: true,
      arrowclassicon: {
        true: "el-icon-video-play",
        false: "el-icon-video-pause"
      },
      arrowflag: true,
      settimer: "",
      xcont: 0,
      alldatas: []
    };
  },
  methods: {
    open_url(resolve) {
      let url = "http://jinwandafiji.club/pw/thread.php?fid=14";
      let opts = { url, headers };
      // console.log(user_agent)
      request(opts, (err, res, body) => {
        if (err) console.error(err);
        this.find_href(body, resolve);
        // resolve(this.find_href(body))
        // console.log(body)
      });
    },
    open_imgUrl(url, callback) {
      let opts = { url, headers };
      // console.log(user_agent)
      request(opts, (err, res, body) => {
        if (err) console.error(err);
        callback(body);
      });
    },
    find_href(html, resolve) {
      // 匹配页面中的链接
      // let b = /<a href =""/gi
      // let b=/<a href=(\"html_data([^<>"\']*)\"|\'([^<>"\']*)\')[^<>]*>/gi;
      let hreflist = [];
      let b = /html_data([^<>"\']*)/gi;
      let hrefs = html.match(b);
      hrefs.forEach((e, i) => {
        if (i % 2 === 0) {
          let href = "http://k6.csnjcbnxdnb.xyz/pw/" + e;
          hreflist.unshift(href);
        }
      });
      console.log(hreflist.length);
      this.find_img(hreflist, resolve);
      // resolve(this.find_img(hreflist))
    },
    find_img(hreflist, resolve) {
      // console.log(hreflist.length)
      let alldatalist = [];
      // for(let i=0 ;i<hreflist.length;i++){
      hreflist.forEach(e => {
        //   console.log(e);
        this.open_imgUrl(e, data => {
          if (data === null || data === undefined) {
            return false;
          } else {
            // 匹配img 的 src 属性
            let srclist = [];
            let b = /http:\/\/p8.urlpic.club\/([^<>"\']*)\.jpg/gi;
            let srcs = data.match(b);
            // console.log(srcs)
            if (srcs === null || srcs === undefined) {
              return false;
            } else {
              srcs.forEach((e, i) => {
                if (i % 2 === 0) {
                  srclist.unshift(e);
                }
              });
            }
            console.log(srclist);
            // 匹配 img 的 title 值
            let t = /\<span id="([^\d\[\]<>"\']*)"\>([^\d\[\]<>"\']*)\[([^<>"\']*)\]\<\/span\>/gi;
            let titles = data.match(t);
            if (titles === null || titles === undefined) {
              return false;
            } else {
              alldatalist.unshift({
                title: titles[0],
                href: srclist,
                star: 0,
                collect: false,
                delete: false,
                download: false
              });
            }
          }
          // console.log(this.alldatas)
        });
      });
      setTimeout(() => {
        this.alldatas = alldatalist;
        this.comover(alldatalist, resolve);
      }, 10000);
      this.alldatas = alldatalist;
      this.comover(alldatalist, resolve);
    },
    comover(data, resolve) {
      if (data.length !== 0) {
        // console.log(`本次加载了${data.length}套`)
        resolve(console.log(`本次加载了${data.length}批`));
      }
    },

    getimgsrc() {
      fs.readFile(file, (err, data) => {
        if (err) console.error(err);
        this.allHrefsTemp = JSON.parse(data.toString());
        // this.deleItemfunc(this.allHrefsTemp);
        this.allHrefs = this.allHrefsTemp;
      });
    },

    deleItemfunc(arr) {
      arr.forEach(e => {
        if (e.delete === false) {
          this.allHrefs.unshift(e);
        }
      });
    },
    // getAllHrefs() {
    //   this.allHrefs = this.allHrefsTemp;
    //   if (localStorage.getItem("deldata")) {
    //     this.delhrefs = JSON.parse(localStorage.getItem("deldata"));
    //   }
    // },

    //save the file
    saveFile() {
      let data = JSON.stringify(this.allHrefsTemp);
      fs.writeFile(file, data, err => {
        if (err) return console.error(err);
        console.log("success");
      });
    },

    showthisFolder(e) {
      this.folderflag = true;
      this.laycont = 0;
      this.hrefs = e;
      this.actflag = true;

      // console.log(this.$refs.allimgdom)
    },
    deletepic(i) {
      // let foldPic= this.$refs.foldPic
      this.$confirm("此操作将删除该文件, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      })
        .then(() => {
          this.hrefs.href.splice(i, 1);
          this.saveFile();
          this.$message({
            type: "success",
            message: "删除成功!"
          });
        })

        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除"
          });
        });
    },

    // 给元素绑定动画
    animateCSS(element, animationName, callback) {
      const node = document.querySelector(element);
      node.classList.add("animated", animationName);

      function handleAnimationEnd() {
        node.classList.remove("animated", animationName);
        node.removeEventListener("animationend", handleAnimationEnd);

        if (typeof callback === "function") callback();
      }

      node.addEventListener("animationend", handleAnimationEnd);
    },

    // 给group元素绑定动画
    animateGroupCSS(element, animationName, callback) {
      element.classList.add("animated", animationName);

      function handleAnimationEnd() {
        element.classList.remove("animated", animationName);
        element.removeEventListener("animationend", handleAnimationEnd);

        if (typeof callback === "function") callback();
      }

      element.addEventListener("animationend", handleAnimationEnd);
    },
    //给元素添加和移除模糊效果
    nodeBlur(e,f){
      const node = document.querySelector(e);
      if(f===true){
        node.classList.add('boxblur')
      }else{
        node.classList.remove('boxblur')
      }
    },

    // topbar 按钮点击事件
    backhome() {
      this.animateCSS(".allpicture", "bounceInRight");
      this.folderflag = false;
      this.laycont = 24;
      this.actflag = false;
      this.allHrefs = [];
      this.allHrefs = this.allHrefsTemp;
      // let imgdoms = document.querySelectorAll('.tImgCard');
      // imgdoms.forEach(e => {
      //   this.animateGroupCSS(e, "bounceInUp");
      // });
    },
    getmore() {
      this.folderflag = false;
      this.actflag = false;
      this.laycont = 24;
      this.allHrefs = this.alldatas;
      // this.animateCSS(".allpicture", "bounceInRight");
      let imgdoms = document.querySelectorAll(".tImgCard");
      imgdoms.forEach(e => {
        this.animateGroupCSS(e, "bounceInUp");
      });
      if (this.alldatas.length === 0) {
        let f1 = () => {
          return new Promise(resolve => {
            this.open_url(resolve);
            // resolve(this.open_url(resolve))
            console.log("f1 ok");
          });
        };
        let f2 = () => {
          return new Promise(resolve => {
            this.allHrefs = this.alldatas;
            console.log("f2 ok");
            resolve("f2 ok");
          });
        };
        let f3 = () => {
          return new Promise(resolve => {
            // this.allHrefsTemp.push.apply(this.allHrefsTemp,this.alldatas);
            let newarr = this.allHrefsTemp.concat(this.alldatas);
            console.log("f3 ok");
            resolve(newarr);
          });
        };
        let f4 = newarr => {
          return new Promise(resolve => {
            this.allHrefsTemp = [...new Set(newarr)];
            console.log("f4 ok");
            resolve(this.allHrefsTemp);
          });

        };
        let f5 = () => {
          return new Promise(resolve => {
            this.saveFile();
            console.log("f4 ok");
            resolve("f4 ok");
          });
        };
        f1()
          .then(f2)
          .then(f3)
          .then(f4)
          .then(f5);
      }
      
    },

    // 我的收藏 collect 点击事件 and 回收中心点击事件
    getTopBarFunc(mainstr) {
      this.folderflag = false;
      this.laycont = 24;
      this.actflag = false;
      this.allHrefs = [];
      let imgdoms = document.querySelectorAll(".tImgCard");

      this.allHrefsTemp.forEach(e => {
        if (mainstr === "collect") {
          // this.animateCSS('.allpicture','bounceInRight');
          imgdoms.forEach(e => {
            this.animateGroupCSS(e, "bounceInUp");
          });
          if (e.collect === true) {
            this.allHrefs.unshift(e);
          }
        } else if (mainstr === "download") {
          // this.animateCSS(".allpicture", "bounceInRight");
          imgdoms.forEach(e => {
            this.animateGroupCSS(e, "bounceInUp");
          });
          if (e.download === true) {
            this.allHrefs.unshift(e);
          }
        }
      });
    },

    showlgpic(e) {
      // const node = document.querySelector('.folderpicture');
      // node.classList.add('boxblur')
      this.nodeBlur('.folderpicture',true)
      this.showlgpicflag = true;
      this.lghref = e;
      this.showtopbarflag = false;
    },
    closethis() {
      // const node = document.querySelector('.folderpicture');
      // node.classList.remove('boxblur')
      this.nodeBlur('.folderpicture',false)
      this.showlgpicflag = false;
      this.showtopbarflag = true;
      clearInterval(this.settimer);
      this.arrowflag = true;
    },

    //click the lgpic function
    maxWindow() {
      this.$refs.topbar.maxfunc();
    },

    // arrow button function
    arrowfunc(o) {
      let arrHref = this.hrefs.href;

      arrHref.forEach((e, i) => {
        if (this.lghref === e) {
          this.xcont = i;
        }
      });
      if (o === "left") {
        this.xcont--;
        this.animateCSS(".lgboximg", "fadeInLeft");

        if (this.xcont === -1) {
          this.xcont = arrHref.length - 1;
          // alert("going start don't click again ")
        }
        this.showlgpic(arrHref[this.xcont]);

        // console.log(this.xcont)
      } else if (o === "right") {
        this.animateCSS(".lgboximg", "fadeInRight");

        this.xcont++;
        if (this.xcont === arrHref.length) {
          this.xcont = 0;
        }
        this.showlgpic(arrHref[this.xcont]);
        // console.log(this.xcont)
      } else if (o === "mid") {
        // 幻灯片播放和停止
        this.arrowflag = !this.arrowflag;
        if (this.arrowflag === true) {
          clearInterval(this.settimer);
        } else {
          console.log(this.xcont);
          console.log(this.arrowflag);
          this.settimer = setInterval(this.setscend, 2200);
        }
      }
    },
    setscend() {
      this.xcont++;
      this.animateCSS(".lgboximg", "fadeInRight");

      if (this.xcont === this.hrefs.href.length) {
        this.xcont = 0;
      }
      this.showlgpic(this.hrefs.href[this.xcont]);
      console.log(this.xcont);
      console.log(this.arrowflag);
    },
    mousemovefunc(e) {
      // console.log(e.pageX, e.pageY,e.screenX,e.screenY)
      let smbarH = this.$refs.smallbar.offsetHeight;
      let smbarX = this.$refs.smallbar.offsetWidth;
      let smbox = this.$refs.smbox;
      let smboxW = smbox.offsetWidth;
      // console.log(smboxW)

      if (e.pageY / smbarH > 0.8) {
        this.smallbarflag = true;
        smbox.scrollLeft = (e.pageX / smbarX) * smboxW * 2;
        if (e.pageX / smbarX < 0.1) {
          smbox.scrollLeft = 0;
        } else if (e.pageX / smbarX > 0.95) {
          smbox.scrollLeft = smboxW * 2.5;
        }
      } else {
        this.smallbarflag = false;
      }
    }
  },
  beforeCreate() {},
  created() {
    this.getimgsrc();
  },
  beforeMount() {},
  mounted() {
    this.animateCSS(".allpicture", "bounceInRight");
  },
  beforeUpdate() {},
  updated() {},
  beforeDestroy() {},
  destroyed() {}
};
</script>

