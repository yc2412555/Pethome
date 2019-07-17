<template>
    <div class="cyq-login">
      <mt-field label="用户名:" placeholder="用户名" ></mt-field>
      <mt-field label="密码:" placeholder="密码" type="password" ></mt-field>
      <mt-button type="primary" class="cyq-login-btn" size="large">登录</mt-button>
      <div class="cyq-login-p">
        <p>短信登录</p>
        <p>忘记密码?</p>
      </div>
    </div>
</template>

<script> 
import { mapActions, mapGetters } from 'vuex'
// import { Toast } from 'mint-ui'
export default {

}
</script>

<style lang="scss">
.cyq-login{
  .mint-cell-wrapper {
    background-color: #fafafa;
    border: 1px solid #f0f0f0;
    margin: 0 15px;
  }
  .mint-field-core{
    background-color: #fafafa;
  }
  .mint-cell:first-child .mint-cell-wrapper {
    margin-top: 30px;
    margin-bottom: 30px;
  }
  .mint-field .mint-cell-title{
    width: 70px;
  }
  .mint-cell:nth-child(2) {
    .mint-cell-wrapper:nth-child(2) {
      margin-bottom: 30px;
      .mint-cell-text{
        padding-left: 15px;
      }
    }
  }
  &-btn {
    background-color: #00ad46;
    width: 92%;
    margin: 0 15px;
  }
  &-p{
    display: inline-block;
    p{
      float: left;
      font-size: 16px;
      padding:15px 59px;
    }
  }
}
</style>
