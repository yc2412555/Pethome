<template>
  <div class="cyq-mine">
    <div class="cyq-mine-top">
      <div class="cyq-mine-top-xinxi">
        <div class="cyq-mine-top-xinxi-photo">
          <!-- <img src="http://cdn.duitang.com/uploads/item/201601/08/20160108194244_JxGRy.thumb.700_0.jpeg" alt=""> -->
        </div>
        <div class="cyq-mine-top-xinxi-info">
          <div class="cyq-mine-top-xinxi-info-name">
            <span>SHHfly</span>
          </div>
          <div class="cyq-mine-top-xinxi-info-chongliang">
            我的宠粮：<span>0</span>g
          </div>
        </div>
      </div>
      <div class="cyq-mine-top-caozuo">
        <div class="pinglun">
          <i class="icon">&#xe628;</i>
          <span>评论回复</span>
        </div>
        <div class="guanzhu">
          <i class="icon">&#xe627;</i>
          <span>关注</span>
        </div>
        <div class="shezhi">
          <i class="icon">&#xe626;</i>
          <span>设置</span>
        </div>
      </div>
    </div>
    <div class="cyq-mine-bottom">

    </div>
  </div>
    
</template>

<script>
export default {

}
</script>

<style lang="scss">
.cyq-mine{
  &-top{
    height: 200px;
    border-bottom: 5px solid #eeeeee;
    &-xinxi{
      height: 80px;
      padding: 20px 0 0 20px;
      &-photo{
        width: 80px;
        height: 80px;
        border-radius: 50%;
        overflow: hidden;
        float: left;
        img{
          width:100%;
          height:100%;
        }
      }
      &-info{
        float: left;
        padding:10px 0 0 20px;
        &-name{
          font-weight: bold;
          line-height: 40px;
        }
        &-chongliang{
          color:#333333;
          font-size: 14px;
        }
      }
    }
    &-caozuo{
      height: 100px;
      display: flex;
      justify-content: space-around;
      align-items: center;
      div{
        display: flex;
        flex-direction: column;
        text-align: center;
        i{
          color:#0ff;
          font-size: 30px;
        }
        span{
          color:#3a3838;
          font-size: 14px;
          line-height: 30px;
        }
      }
    }
  }
}
  
</style>
