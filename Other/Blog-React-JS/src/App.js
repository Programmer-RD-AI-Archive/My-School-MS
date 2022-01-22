import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import Home from "./screens/Home";
import Sign_Up from "./screens/Sign_Up";
import useFirebase from "./db/useFirebase"
function App() {
  const { app, firebaseConfig, analytics } = useFirebase();
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path="/">
            <NavBar
              lists={[
                { Name: "Home", URL: "/" },
                { Name: "Sign Up", URL: "/Sign/Up" },
                { Name: "Sign In", URL: "/Sign/In" },
                { Name: "About Me", URL: "/About/Me" },
                { Name: "Contact Us", URL: "/Contact/Us" },
              ]}
            />
            <Home />
          </Route>
          <Route exact path="/Sign/Up">
            <NavBar
              lists={[
                { Name: "Home", URL: "/" },
                { Name: "Sign Up", URL: "/Sign/Up" },
                { Name: "Sign In", URL: "/Sign/In" },
                { Name: "About Me", URL: "/About/Me" },
                { Name: "Contact Us", URL: "/Contact/Us" },
              ]}
            />
            <Sign_Up />
          </Route>
          <Route exact path="/Sign/In">
            <NavBar
              lists={[
                { Name: "Home", URL: "/" },
                { Name: "Sign Up", URL: "/Sign/Up" },
                { Name: "Sign In", URL: "/Sign/In" },
                { Name: "About Me", URL: "/About/Me" },
                { Name: "Contact Us", URL: "/Contact/Us" },
              ]}
            />
          </Route>
        </Switch>
      </Router>
      <div className="footer">
        <p>Made by Programmer-RD-AI</p>
      </div>
    </div>
  );
}

export default App;
