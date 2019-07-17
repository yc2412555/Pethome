<template>
  <div class="details" v-if="isDataSuc">
    <div class="details-main">
      <div class="swiper-container">
        <div class="swiper-wrapper">
          <div class="swiper-slide" v-for="banner in banners" :key="banner.id">
            <img :src="src+banner">
          </div>
        </div>
        <!-- 如果需要分页器 -->
        <div class="swiper-pagination"></div>
      </div>
      <div class="details-main-content">
        <!-- <p class="title">{{productInfo.product_name}} {{otherInfo.color_name}} {{otherInfo.spec_value}}</p> -->
        <p class="title">{{title}}</p>
        <!-- <p class="information" v-html="productInfo.selling_points"></p> -->
        <span class="price">￥{{price | toFixed2}}元</span>
        <!-- <span class="price">￥{{price}}元</span> -->
      </div>
      <!-- <div class="promo-sell">
        <div class="title">促销</div>
        <div class="promo-info">
          <p><i class="wrap-txt">赠品</i>&nbsp;<span>送红魔3电竞向量保护套</span></p>
          <p class="spec" style="" hb1="true"><i class="wrap-txt">分期</i>&nbsp;<span>享受花呗6期,免息分期</span></p>
          <p><i class="wrap-txt">积分</i>&nbsp;<span>购买即赠积分，积分可抵现</span></p>
          <p><i class="wrap-txt">包邮</i>&nbsp;<span>青铜及以下满59、白银满39、黄金及以上包邮</span></p>
        </div>
      </div> -->
      <div class="seletGroup">
        <div class="coupon" v-show="hasCoupon">
          <div class="coupon-l">领券</div>
          <div class="coupon-r" v-html="productInfo.coupon_keyword">
            <!-- <span ></span><em>&gt;</em> -->
            <!-- 300元红魔3手机RNG.M助威券 -->
          </div>
        </div>
        <div class="promo-sell">
          <div class="title">促销</div>
          <div class="promo-info">
            <p><i>赠品</i><span>送红魔3电竞向量保护套</span></p>
            <p class="spec" style="" hb1="true"><i class="wrap-txt">分期</i><span>享受花呗6期,免息分期</span></p>
            <p><i>积分</i><span>购买即赠积分，积分可抵现</span></p>
            <p><i>包邮</i> <span>青铜及以下满59、白银满39、黄金及以上包邮</span></p>
          </div>
        </div>
      </div>

    </div>
    <div class="details-collect">
      <!-- <span class="incon">&#xe625;</span>
      <span class="incon">&#xe62f;</span> -->
      <span class="add-to-cart" @click.stop="addToCart({
        id:sid,
        image:src+banners[0],
        title,
        price
      })">加入购物车
      </span>
      <span class="jump-to-cart" @click="jumpToCart">
        去购物车结账
        <b class="count">{{totalCount | mt100}}</b>
      </span>
    </div>
  </div>
  <div class="details-nothing" v-else>
    <div>
      <p>商品加载失败了</p>
      <p>请返回重试</p>
      <p>怎么肥四？小老弟</p>
      <span></span>
    </div>
  </div>
</template>

<script>
import Swiper from 'swiper'
import swiperCss from 'swiper/dist/css/swiper.min.css'
import * as ajax from '@/request/index'
import {
  mapMutations,
  mapGetters
} from 'vuex'

export default {
  data () {
    return {
      src: 'https://oss.static.nubia.cn/',
      id: '',
      sid: '',
      productInfo: {},
      banners: {},
      otherInfos: '',
      otherInfo: '',
      price: '',
      title: '',
      isDataSuc: true,
      hasCoupon: false
    }
  },
  computed: {
    ...mapGetters(['totalCount'])
  },
  created () {
    // console.log(this.$route)
    this.id = Number(this.$route.query.id)
    this.sid = Number(this.$route.query.sid)
    // console.log(this.id, this.sid)
    this.getDetail()
  },
  // beforeRouteEnter (to, from ,next) {
  //   // console.log(to, from)
  //   next(vm => {
  //     vm.getDetail()
  //   })
  // },
  // beforeRouteUpdate (to, from ,next) {
  //   this.getDetail()
  //   next()
  // },
  // updated () {
  //   this.id = Number(this.$route.query.id)
  //   this.sid = Number(this.$route.query.sid)
  //   this.getDetail()
  // },
  methods: {
    // addToCart () {
    //   console.log(this.id)
    // },
    // ...mapGetters(['totalCount']),
    ...mapMutations(['addToCart']),
    jumpToCart () {
      this.$router.push('/cart')
    },
    getDetail () {
      // console.log(this.id)
      ajax.getProduct(this.id).then(resp => {
        // console.log(resp)
        this.productInfo = resp
        if (this.productInfo.coupon_keyword) this.hasCoupon = true
        this.otherInfos = resp.product_specs
        // console.log(this.otherInfos)
        // 判断款式：颜色、存储、内存
        this.otherInfos.forEach(item => {
          if (item.id === this.sid) {
            this.otherInfo = item
          }
        })
        // console.log(this.otherInfo)
        if (!this.otherInfo) {
          this.isDataSuc = false
        }
        this.banners = this.otherInfo.images
        this.price = Number(this.otherInfo.price)
        this.title = resp.product_name + ' ' + this.otherInfo.color_name + ' ' + this.otherInfo.spec_value
        // console.log(this.title)
        // console.log(this.banners)
        // console.log(this.price)
        // 异步数据返回后再生成banner，否则先生成再渲染就不会循环
        // 但是created不会操作DOM
        // 通过异步返回的数据去操作DOM，那就放到nextTick里去执行
        this.$nextTick().then(() => {
          if (this.banners.length !== 1) this.initSwiper()
        })
      })
    },
    initSwiper () {
      let mySwiper = new Swiper('.swiper-container', {
        // autoplay: true,
        // 触碰后自动切换也不会停止
        autoplay: {
          disableOnInteraction: false
        },
        loop: true, // 循环模式选项
        // 如果需要分页器
        pagination: {
          el: '.swiper-pagination'
          // bulletClass: "banner-btn",
          // bulletActiveClass: "banner-btn-ac"
        }
      })
    }
  }
}
</script>

<style lang="scss">
.details {
  height: 100%;
  display: flex;
  flex-direction: column;

  &-main {
    overflow-x: hidden;
    flex: 1;
    .swiper-container {
      width: 100%;
      padding-bottom: 10px;
      border-bottom: 1px solid #ccc;
      img {
        width: 100%;
      }
    }

    &-content {
      margin-bottom: 1px;
      position: relative;
      font-size: 18px;
      background: #fff;
      line-height: 1.5;
      padding: 10px 16px;
      text-align: left;
      margin-top: 1px;

      .title {
        width: 100%;
        justify-content: space-between;
        align-items: center;
        color: rgb(25,25,25);
        font-weight: bold;
      }

      .information {
        color: rgb(255, 77, 77);
        font-weight: 800;
        margin-bottom: 10px;

        span {
          font-size: 15px!important;
        }
      }

      .price {
        color: #ff4d4d;
        font-size: 18px;
        display: inline-block;
        width: 100%;
      }
    }
    .seletGroup {
      width: 100%;
      display: inline-block;
      background: #fff;
      margin: 3px 0;
      padding: 3px 10px;
      em {
        color: #868686;
        font-size: 20px;
      }
      .coupon {
        font-size: 13px;
        height: 3.5rem;
        display: flex;
        // justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid rgb(238,238,238);
        .coupon-l {
          width: 15%;
          font-size: 15px;
          color: rgb(134,134,134);
          }
          .coupon-r {
            width: 80%;
            display: flex;
            overflow: auto;
            justify-content: space-between;
          }
          span {
            display: block;
            background: rgb(255,94,94);
            color: #fff;
            border-radius: 1rem;
            margin-right: 0.8rem;
            display: block;
            position: relative;
            max-width: 240px;
            padding: 0.25rem 1.1rem;
            line-height: 18px;
          }
        }
      }

      .promo-sell {
        background: #fff;
        width: 100%;
        display: flex;
        /* justify-content: space-between; */
        /* align-items: flex-start; */
        border-bottom: 1px solid rgb(238,238,238);
        padding: 1rem 0px;

        .title {
          width: 15%;
          font-size: 0.9rem;
          color: rgb(134,134,134);
        }
        .promo-info {
          width: 85%;
          display: inline-block;
          p {
            width: 100%;
            margin-bottom: 0.4rem;
            color: rgb(53,53,53);
            display: flex;
            justify-content: flex-start;
            align-items: flex-start;
            i{
              margin-right: 0.75rem;
              color: rgb(255,94,94);
              padding: 0rem 0.5rem;
              border-radius: 1rem;
              border: 1px solid rgb(255,94,94);
              /* background: white; */
              font-size: 0.9rem;
            }
            span {
              display: inline-block;
              width: 75%;
              font-size: 0.9rem;
            }
          }
        }
      }
    }

    &-collect {
      // position: fixed;
      width: 100%;
      height: 60px;
      // bottom: 0;
      // left: 0;
      display: flex;
      justify-content: space-around;
      align-items: center;
      span {
        color: #fff;
        background: #ff4d4d;
        text-align: center;
        width: 40%;
        display: inline-block;
        height: 36px;
        line-height: 36px;
        border-radius: 50px;
        border: none;
        font-size: 14px;
      }
      .jump-to-cart {
        background: #999;
        position: relative;
        b.count {
          position: absolute;
          left: 120px;
          top: -10px;
          min-width: 20px;
          height: 20px;
          font-size: 10px;
          line-height: 20px;
          background-color: #e00;
          color: #fff;
          border-radius: 10px;
          text-align: center;
        }
      }
    }

  &-nothing {
    margin: 0 auto;
    margin-top: 100px;
    text-align: center;
    p {
      height: 40px;
      line-height: 40px;
    }
    span {
      display: block;
      width: 260px;
      height: 260px;
      margin: 0 auto;
      background: url(https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1311782433,1638354004&fm=27&gp=0.jpg);
    }
  }
}

@font-face {
  font-family: 'iconfont';  /* project id 1169919 */
  src: url('//at.alicdn.com/t/font_1169919_0uzyljx5cvxc.eot');
  src: url('//at.alicdn.com/t/font_1169919_0uzyljx5cvxc.eot?#iefix') format('embedded-opentype'),
  url('//at.alicdn.com/t/font_1169919_0uzyljx5cvxc.woff2') format('woff2'),
  url('//at.alicdn.com/t/font_1169919_0uzyljx5cvxc.woff') format('woff'),
  url('//at.alicdn.com/t/font_1169919_0uzyljx5cvxc.ttf') format('truetype'),
  url('//at.alicdn.com/t/font_1169919_0uzyljx5cvxc.svg#iconfont') format('svg');
}

.incon {
  font-family: 'iconfont';
  font-size: 24px;
  color: #5a5a5a;
}
</style>
