<template>
  <div class="send-wrapper">
    <!-- <div class="send-text-wrapper"> -->
    <textarea placeholder="请输入内容" rows="8" v-model="inuptText" class="send-text" />
    <!-- </div> -->
    <div class="send-public-wrapper">
      <label class="public-wrapper">
        <span class="send-public-span">公开：</span>
        <vantSwitch
          v-model="isPublic"
          class="send-public-switch"
          @change="switchChange"
          size="14px"
        />
        <!-- <van-switch
          v-model="checked"
          size="24px"
        /> -->
      </label>
      <span class="send-button" @click="send">发送</span>
    </div>
    <div class="send-tags-wrapper">
      <span class="send-tags-span">标签：</span>
      <label v-for="item in tags" :key="item.t_id">
        <input type="checkbox" class="checkbox" @change="toggleTags(item.t_id)">
        <span class="tag" >{{item.t_content}}</span>
      </label>
    </div>
    <!-- <Switch  v-model="isPublic"></Switch> -->
    <Uploader
      multiple
      v-model="fileList"
      class="select-button"
      :after-read="afterRead"
      :max-count="2"
      :before-read="beforeRead"
    ></Uploader>
  </div>
</template>
<script>
import * as ajax from "@/request/index"
import { Toast, MessageBox } from "mint-ui"
// import { Switch } from 'vant'
import Uploader from 'vant/lib/uploader';
import vantSwitch from 'vant/lib/switch';
import 'vant/lib/uploader/style';
import 'vant/lib/switch/style';
export default {
  props: {},
  data() {
    return {
      inuptText: "",
      tags: [],
      checkedTags: [],
      isPublic: true,
      fileList: [],
      imgs: []
    }
  },
  components: { Uploader, vantSwitch },
  methods: {
    send() {
      // console.log(this.inuptText)
      // console.log(this.checkedTags)
      if (this.inuptText === "") return Toast("请输入内容")
      if (this.checkedTags.length === 0) return Toast("请至少选择一个标签")
      MessageBox.confirm("确定发送吗？").then(() => {
        // console.log(action)
        let isPublicNum = Number(this.isPublic)
        // console.log(isPublicNum)
        ajax.sendDynamic(this.inuptText, this.checkedTags, isPublicNum, this.imgs).then(resp => {
          // console.log(this.inuptText, this.checkedTags, isPublicNum)
          if(resp.code === 200){
            let instance = Toast("发送成功 即将返回宠友圈")
            setTimeout(() => {
              instance.close()
              this.$router.go(-1)
            }, 2000)
          } else {
            // console.log('fail')
            Toast('发送失败，请重试')
          }
        })
      })
    },
    afterRead(file) {
      // console.log(file)
      this.imgs.push(file.content)
      // console.log(this.imgs)
    },
    beforeRead(file) {
      if (file.type == 'image/jpeg' || file.type == 'image/png' || file.type == 'image/x-icon' || file.type == 'image/gif') {
        return true
      } else {
        Toast('请上传2张图片')
        return false
      }
    },
    toggleTags(id) {
      // console.log(id)
      if(this.checkedTags.indexOf(id) === -1) {
        this.checkedTags.push(id)
        // console.log(this.checkedTags)
      } else {
        this.checkedTags.forEach((item, index) => {
          if (item === id) this.checkedTags.splice(index, 1)
        })
        // console.log(this.checkedTags)
      }
    },
    switchChange() {
      // this.isPublic = !this.isPublic
      // console.log(this.isPublic)
    }
  },
  created() {
    ajax.getTags().then(resp => {
      // console.log(resp)
      this.tags = resp.data
      // console.log(this.tags)
    })
  }
}
</script>
<style lang="scss" scoped>
.send-wrapper {
  // width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 10px;
  margin: 0 auto;
  .send-text {
    // display: block;
    // height: 200px;
    width: 90%;
    margin: 0 auto;
    border: 2px solid #eee;
    outline: none;
    padding: 8px;
  }
  .send-public-wrapper {
    // display: flex;
    // margin-top: 20px;
    .public-wrapper {
      display: flex;
      padding-left: 25px;
      height: 40px;
      line-height: 40px;
      width: 100px;
      float: left;
    }
    .send-public-span {
      font-size: 14px;
    }
    .send-public-switch {
      margin-top: 12px;
      .mint-switch-core {
        width: 40px !important;
        height: 20px !important;
        &::before {
          width: 37px !important;
          height: 18px !important;
        }
        &::after {
          width: 18px !important;
          height: 18px !important;
        }
      }
    }
    .select-button {
      // font-family: "幼圆";
      float: left;
      margin-left: 25px;
      width: 166px;
    }
    .send-button {
      display: block;
      width: 50px;
      height: 20px;
      border: 1px solid #666;
      float: right;
      margin-right: 25px;
      margin-top: 10px;
      text-align: center;
      line-height: 20px;
      background: #eee;
      border-radius: 5px;
      // font-family: "幼圆";
      font-size: 14px;
    }
  }
  .send-tags-wrapper {
    margin-top: 5px;
    padding-left: 20px;
    .send-tags-span {
      font-size: 14px;
    }
    .checkbox {
      display: none;
    }
    label {
      display: inline-block;
      margin: 3px 0;
    }
    .tag {
      display: inline-block;
      // width: 30px;
      padding: 0 4px;
      height: 20px;
      line-height: 20px;
      text-align: center;
      font-size: 12px;
      border: 1px solid #ccc;
      border-radius: 5px;
      margin: 0 4px;
    }
    input:checked {
      + span {
        background: #ccc;
      }
    }
  }
  .van-uploader {
    margin-top: 15px;
    padding: 0 10px;
  }
}
</style>