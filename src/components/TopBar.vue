<style scoped>
div {
  -webkit-app-region: drag;
  user-select: none;
}
.el-menu {
  /*border-top: 3px rgb(255, 0, 0) solid;*/
  z-index: 99;
  width: 100%;
  background: #fdf4ec;
}
.el-menu li {
  -webkit-app-region: no-drag;
}
li.el-menu-item{
transition: all .5s;
}
.is-active{
  color: #fffdfb !important;
  border-bottom-color: red !important;
  background: red !important;
}
li.el-menu-item:hover{
  /* color: #effdfa !important;
  background: red !important; */
  border-bottom-color: red !important;
}
.el-menu--horizontal > .el-menu-item {
  float: left;
  height: 30px;
  line-height: 30px;
}
.closeicon {
  -webkit-app-region: no-drag;
  position: absolute;
  right: 0%;
  top: 0px;
  z-index: 100;
}
.closeicon i {
  cursor: pointer;
  width: 60px;
  height: 25px;
  padding-top: 5px;
  text-align: center;
  color: rgb(163, 163, 163);
  transition: all 0.4s;
}
.closeicon i:hover {
  color: rgb(255, 255, 255);
  background: rgb(97, 97, 97);
}
.closeicon i:nth-child(3):hover {
  color: white;
  background: rgb(255, 25, 25);
}
</style>
<template>
<div>
  <el-menu
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
    text-color="#ff2222"
    active-text-color="#2222ff"
    @select="handleSelect"
  >
    <el-menu-item index="1" @click="$emit('backhomefunc')"><i class="el-icon-house"></i> 主页</el-menu-item>
    <el-menu-item index="2"  @click="$emit('getTopBarfunc','collect')"><i class="el-icon-star-off"></i>我的收藏</el-menu-item>
    <!-- <el-menu-item index="3" @click="$emit('getTopBarfunc','deleted')"><i class="el-icon-delete"></i>回收中心</el-menu-item> -->
    <el-menu-item index="4" @click="$emit('getTopBarfunc','download')"><i  class="el-icon-download"></i>下载中心</el-menu-item>
    <el-menu-item index="5"  @click="$emit('getmore')"><i class="el-icon-loading"></i>加载更多</el-menu-item>
  </el-menu>
  <div class="closeicon">
    <i class="el-icon-minus" @click="minfunc()"></i>
    <i class="el-icon-full-screen" @click="maxfunc()"></i>
    <i class="el-icon-close" @click="closefunc()"></i>
  </div>
  <div class="line"></div>
  </div>
</template>
 
<script>
import { ipcRenderer } from "electron";
export default {
  data() {
    return {
      activeIndex: "1",
      activeIndex2: "1"
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      // console.log(key, keyPath);
    },
    closefunc() {
      ipcRenderer.send("close");
    },
    maxfunc() {
      ipcRenderer.send("max");
    },
    minfunc() {
      ipcRenderer.send("min");
    }
  }
};
</script>