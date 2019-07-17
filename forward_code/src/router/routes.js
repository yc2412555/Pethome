const Consul = () => import('@/views/Consul')
const Domes = () => import('@/views/Domes')
const Favour = () => import('@/views/Favour')
const SendDynamic = () => import('@/views/SendDynamic')
const Nearby = () => import('@/views/Nearby')
const Mine = () => import('@/views/Mine')
const Login = () => import('@/views/Login')
const CyqFooter = () => import('@/components/CyqFooter')
const CyqHeader = () => import('@/components/CyqHeader')
const FavourHeader = () => import('@/components/FavourHeader')
const SendHeader = () => import('@/components/SendHeader')
const Classfydog = () => import('@/views/Classfydog')
const Dogdetail = () => import('@/views/Dogdetail')
const Classfycat = () => import('@/views/Classfycat')
const Catdetail = () => import('@/views/Catdetail')

export default [
  {
    path: '/',
    redirect: '/favour',
    meta: {}
  },
  {
    path: '/nearby',
    name: 'nearby',
    // component: Nearby,
     components: {
      default: Nearby,
      header: CyqHeader,
      footer: CyqFooter,
    },
    meta: {
      isTabbar: true,
      title: '附近',
      icon: '&#xe68a;'
    }
  },
  {
    path: '/domes',
    name: 'domes',
    // component: Domes,
    components: {
      default: Domes,
      header: CyqHeader,
      footer: CyqFooter,
    },
    meta: {
      isTabbar: true,
      title: '宠物驯养',
      icon: '&#xe612;'
    }
  },
  {
    path: '/favour',
    name: 'favour',
    components: {
      default: Favour,
      header: FavourHeader,
      footer: CyqFooter,
    },
    meta: {
      isTabbar: true,
      title: '宠友圈',
      icon: '&#xe68c;'
    }
  },
  {
    path: '/send',
    name: 'send',
    components: {
      default: SendDynamic,
      header: SendHeader
    },
    meta: {
      isTabbar: false,
      title: '发布动态'
    }
  },
  {
    path: '/consul',
    alias: '/',
    name: 'consul',
    // component: Consul,
    components: {
      default: Consul,
      // header: CyqHeader,
      footer: CyqFooter,
    },
    meta: {
      isTabbar: true,
      title: '宠物咨询',
      icon: '&#xe610;'
    }
  },
  
  {
    path: '/classfydog',
    name: 'classfydog',
    components: {
      default: Classfydog
    },
    meta:{}
  },
  {
    path: '/dogdetail/:id',
    name: 'dogdetail',
    components: {
      default: Dogdetail
    },
    meta: {}
  },
  {
    path: '/classfycat',
    name: 'classfycat',
    components: {
      default: Classfycat
    },
    meta:{}
  },
  {
    path: '/catdetail/:id',
    name: 'catdetail',
    components: {
      default: Catdetail
    },
    meta: {}
  },
  {
    path: '/mine',
    name: 'mine',
    // component: Mine,
    components: {
      default: Mine,
      // header:CyqHeader,
      footer: CyqFooter,
    },
    meta: {
      isTabbar: true,
      title: '我的',
      icon: '&#xe687;'
    }
  },
  {
    path: '/login',
    name: 'login',
    components: {
      default: Login,
      footer: CyqFooter
    },
    meta: {
      title: '登录'
    }
  }
]