
import './App.css';
import Home from './Pages/Home';
import { useEffect,useState } from 'react';
import productApi from "./Api/productApi"
import Pagination from './Components/Pagination';
function App() {
  const [data,setData] = useState([])

  

  useEffect(()=>{
    const fetchProducts = async () =>{
      const params = {
        _limit: 10
      }
      const productList = await productApi.getAll(params);
      console.log(productList)
      setData(productList)
    }
    fetchProducts()
  },[])  

  


  return (
    <div className="App">
      <Home/>
      <ul>
        {data.map((item)=>{
          return <li key = {item.id}> Tên sản phẩm: {item.name} - Mã sản phẩm: {item.id}</li>
        })}
      </ul>
      
      
      
      
    </div>


  );
}

export default App;
