import axios from 'axios'
import { Indicator } from 'mint-ui'
const ajax = axios.create()
ajax.interceptors.request.use(config => {
  // config.data = {
  //   token: 'abc'
  // }
  Indicator.open({
    text: '加载中...',
    spinnerType: 'fading-circle'
  })
  return config
})
ajax.interceptors.response.use(resp => {
  Indicator.close()
  if (resp.status === 200) {
    return resp.data
  } else {
    return {
      status: 400,
      msg: '网络错误'
    }
  }
})
export const getDynamics = () => ajax.get('/api/v1/dynamics')
export const getTags = () => ajax.get('/api/v1/tags')
export const sendDynamic = (text, checkedTags, isPublic) => ajax.post('/api/v1/dynamic/publishment', {
      text_content: text,
      t_id: checkedTags,
      is_public: isPublic
    })
// export const sendDynamic = (text, checkedTags) => axios({
//   method: 'post',
//   url: '/api/v1/dynamic/publishment',
//   data: {
//     text_content: text,
//     t_id: checkedTags
//   }
// })
export const toCollection = (id) => ajax.post('/api/v1/dynamic/collection/', {d_id: id})
export const toLike = (id) => ajax.post('/api/v1/dynamic/pride/', {d_id: id})
export const toReply = (id, text) => ajax.post('/api/v1/dynamic/reversion', {d_id: id, c_content: text})
export const getDogs = () =>  ajax.get('/api/v1/dogsVaries')
export const getDogDetail = (id) => ajax.get(`/api/v1/dogsVaries/${id}`)
export const getCats = () => ajax.get('/api/v1/catsVaries')
export const getCatDetail = (id) => ajax.get(`/api/v1/catsVaries/${id}`)