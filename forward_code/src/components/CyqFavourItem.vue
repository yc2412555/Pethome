<template>
  <div class="cyqItem">
    <!-- 需要路由跳转时，使用 -->
    <!--  <router-link tag="li" v-for="tabbar in tabbars" :key="tabbar.name" :to="tabbar.path"> -->
    <div class="cyqItem-top">
      <img :src="user.u_pic" />
      <p>{{user.u_name}}</p>
      <span> {{pub_time}}</span>
    </div>
    <div class="cyqItem-content">
      <span>{{text_content}}</span>
    </div>
    <div class="cyqItem-center">
      <img v-for="p in path" :key="p.p_id" :src="p.p_path" />
    </div>
    <!-- 渲染数据  -->
    <ul class="cyqItem-bottom">
      <li class="cyqItem-bottom-li" @click="toLike">
        <i :class="isLike?'activeIcon icon':'icon'" v-html="'&#xe66f;'" ></i>
        <span class="likeBtn">点赞</span>
        <Badge class="badge">{{g_counts}}</Badge>
      </li>
      <li class="cyqItem-bottom-li" @click="toCollect">
        <i :class="isCollection?'activeIcon icon':'icon'" v-html="'&#xe639;'"></i>
        <span class="collectBtn">收藏</span>
      </li>
      <li class="cyqItem-bottom-li" @click="toggleComments">
        <i :class="isCommentShow?'activeIcon icon':'icon'" v-html="'&#xe66e;'"></i>
        <span class="commentBtn">评论</span>
        <Badge class="badge">{{comments.length}}</Badge>
        <!--  -->
      </li>
    </ul>
    <ul v-show="isCommentShow" class="cyqItem-bottom-ul-li" ref="commentsUl">
      <li v-for="comment in comments" :key="comment.c_id">
        <i>{{comment.user.u_name}}</i>
        <b>:</b>
        <span>{{comment.c_content}}</span>
      </li>
      <li class="commentLi">
        <input class="commentInput" type="text" placeholder="请输入你的妙语" v-model="myComment">
        <span class="commentSendBtn" @click="sendMyComment">发送</span>
      </li>
      <!-- 
        :c_content="comment.c_content"
      :u_name="comment.user.u_name"
        -->
    </ul>
  </div>
</template>
<script>
import { Toast, Badge, MessageBox } from 'mint-ui'
import * as ajax from "@/request/index"
import {
  mapMutations
} from 'vuex'
export default {
  data() {
    return {
      isCommentShow: false,
      myComment: '',
      isLike: false,
      isCollection: false
    }
  },
  props: ["comments", "id", "g_counts", "path", "pub_time", "text_content", "user"],
  components:{
    Badge
  },
  methods: {
    ...mapMutations([
      'addToLikes',
      'addToCollection'
    ]),
    toggleComments() {
      this.isCommentShow = !this.isCommentShow
      // console.log(this.isCommentShow)
    },
    toLike() {
      // console.log(e.target)
      // console.log(this.id)
      if(!this.isLike){
        ajax.toLike(this.id).then(resp => {
          // console.log(resp)
          this.addToLikes(this.id)
          Toast('点赞成功')
          console.log('已点赞:', window.localStorage.cyqLikes)
        })
      } else {
        Toast('点赞取消')
      }
      this.isLike = !this.isLike
      console.log(this.isLike)
    },
    toCollect() {
      if(!this.isCollection){
        ajax.toCollection(this.id).then(resp => {
          this.addToCollection(this.id)
          Toast('收藏成功')
          console.log('已收藏:', window.localStorage.cyqCollection)
        })
      } else {
        Toast('移出收藏')
      }
      this.isCollection = !this.isCollection
    },
    sendMyComment() {
      console.log(this.myComment)
      if(this.myComment !== ''){
        MessageBox.confirm("确定发送吗？").then(() => {
          ajax.toReply(this.id, this.myComment).then(resp => {
            console.log(resp)
            if(resp.code === 200){
              Toast("留言成功")
              this.$emit('sendSuccess', 200)
            }
          })
        })
      } else {
        Toast('留言不能为空！')
      }
    }
  },
  created() {
    // console.log(this.text_content)
  }
}
</script>

<style lang="scss" scoped>
.cyqItem {
  // height: 140px;
  // background: yellowgreen;
  background: #fff;
  &-top {
    padding-top: 14px;
    height: 30px;
    background: #fff;
    font-size: 14px;
    img {
      float: left;
      height: 30px;
      width: 30px;
      margin-left: 10px;
      border-radius: 15px;
      // background: blue;
    }
    p {
      float: left;
      line-height: 30px;
      margin-left: 10px;
    }
    span {
      float: right;
      line-height: 30px;
      margin-right: 10px;
      font-size:12px;
    }
  }
  &-content {
    font-size: 14px;
    margin-top: 5px;
    // height: 50px;
    span {
      display: block;
      // font-family: PingFangSC-Regular;
      // font-size: 16px;
      // letter-spacing: 2px;
      line-height: 20px;
      overflow:hidden;
      // text-overflow:ellipsis;
      // white-space: normal;
      // display:-webkit-box;
      // -webkit-box-orient:vertical;
      // -webkit-line-clamp:2;
    }
  }
  &-center {
    // height: 150px;
    // background: red;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 10px 0;
    img {
      // height: 90%;
      width: 48%;
    }
  }
  &-bottom {
    // background: yellow;
    // height: 100%;
    display: flex;
    border-top: 1px solid #dedede;
    justify-content: space-around;
    text-align: center;
    padding-bottom: 5px;
    &-li {
      // background: red;
      text-align: center;
      align-items: flex-end;
      width: 100px;
      position: relative;
      i, .activeIcon {
        display: block;
        font-size: 24px;
        line-height: 32px;
        // color: red;
      }
      .activeIcon {
        color: #e00;
      }
      span {
        font-size: 12px;
        line-height: 20px;
      }
      .badge {
        // display: none;
        padding: 0;
        font-size: 8px;
        width: 14px;
        height: 14px;
        line-height: 14px;
        position: absolute;
        top: 5px;
      }
    }
  }
  &-bottom-ul-li {
    li {
      display: flex;
      height: 30px;
      line-height: 30px;
      // background: blue;
      span {
        width: 80%;
        margin-right: 10px;
        // font-family: PingFangSC-Regular;
        font-size: 12px;
        overflow:hidden;
        text-overflow:ellipsis;
        white-space: normal;
        display:-webkit-box;
         -webkit-line-clamp: 1;
        -webkit-box-orient:vertical;
      }
      i, b{
        // font-family: PingFangSC-Regular;
        font-size: 12px;
        padding: 0 4px;
      }
    }
    .commentLi {
      margin-top: 10px;
      display: flex;
      flex-direction: row;

      .commentInput {
        outline: none;
        height: 20px;
        flex: 1;
        line-height: 20px;
        border: 1px solid #333;
        border-radius: 5px;
        font-size: 12px;
        padding: 0 10px;
      }
      .commentSendBtn {
        display: block;
        width: 40px;
        height: 20px;
        line-height: 20px;
        text-align: center;
        background: #ddd;
        float: right;
        border-radius: 5px;
        margin-left: 20px;
        border: 1px solid #333;
        // font-family: '幼圆';
      }
    }
  }
}
</style>
