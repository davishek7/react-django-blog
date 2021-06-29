import React, { useEffect, useState} from 'react';
import './App.css'
import PostLoadingComponent from './components/PostLoading';
import Posts from './components/Posts'

const App = () => {

  const PostLoading = PostLoadingComponent(Posts)
  const[appState,setAppState] = useState({
    loading:false,
    posts:null,
  });

  useEffect(()=>{
    setAppState({loading:true})
    const apiUrl = 'http://127.0.0.1:8000/api/';
    fetch(apiUrl)
      .then((data)=>data.json())
      .then((posts)=>{
        setAppState({loading:false,posts:posts})
      });
  },[setAppState]);

  return (
    <div className="App">
      <h1>Latest Posts</h1>
      <PostLoading isLoading={appState.loading} posts={appState.posts} />
    </div>
  )
}

export default App
