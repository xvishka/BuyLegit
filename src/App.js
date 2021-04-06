import './App.css';
import Footer from './component/Footer';
import HomeBar from './component/HomeBar';
import NavBar from './component/NavBar';
import Cards from './component/Cards';
import Login from './component/Login';



function App() {
  return (
    <div className="page container">
      <NavBar/>
      <HomeBar/>   
      
      <Cards/>
      <Footer/>
    </div>
  );
}

export default App;
