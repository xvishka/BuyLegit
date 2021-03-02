import './App.css';
import Svg from '../src/assets/Frame_1.svg';

function App() {
  return (
    <div className="App">
      <nav className="site-nav grid">
          <div className="logo">
            <img src={Svg} alt="React Logo"/>
          </div>
          <ul>
              <li>
                <form className="search">
                    <input type="text" name="name" placeholder="Enter product name"/>
                </form>
              </li>
              <li>
                <select name="dropdown" id="dropdown">
                      <option value="iPhone Covers">iPhone Covers</option>
                      <option value="Smart Watches">Smart Watches</option>
                </select>
              </li>
          </ul>
      </nav>
      <section className="bar grid">
          <ul>
            <li>home {'>'}</li>
          </ul>
      </section>
      <section className="cover">
        <div className="text">
          <h3>Welcome to BuyLegit</h3>
          <h4>buylegit helps you to pick an original product from ebay. we ensure you will always pay the original price and your choice of product is safe from overpriced listings</h4>
        </div>
      </section>
      <section className="cat1 grid">
        <h2>Smart Watches</h2>
        <div>
        </div>
      </section>

      <div className='footerDiv'>  
            <ul id='footerDes'> 
               <li> Home </li>
               <li> Categories </li>
               <li> Visit eBay </li>
            </ul>
      </div>
    </div>
  );
}

export default App;
