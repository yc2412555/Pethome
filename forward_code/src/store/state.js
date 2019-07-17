export default {
  likes: JSON.parse(window.localStorage.getItem('cyqLikes')) || [],
  collection: JSON.parse(window.localStorage.getItem('cyqCollection')) || []
}