import {
  ADD_TO_COLLECTION,
  ADD_TO_LIKES
} from './mutationsTypes'

export default {
  [ADD_TO_LIKES] (state, id) {
    if(state.likes.indexOf(id)===-1){
      state.likes.push(id)
    } else {
      state.likes.forEach((item, index) => {
        if (item === id) state.likes.splice(index, 1)
      })
    }
  },
  [ADD_TO_COLLECTION] (state, id) {
    if(state.collection.indexOf(id)===-1){
      state.collection.push(id)
    } else {
      state.collection.forEach((item, index) => {
        if (item === id) state.collection.splice(index, 1)
      })
    }
  }
}