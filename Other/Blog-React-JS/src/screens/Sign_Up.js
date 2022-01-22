import {
  FormControl,
  InputAdornment,
  InputLabel,
  OutlinedInput,
  TextField,
  Button,
} from "@mui/material";
import { useState } from "react";
import {
  getAuth,
  createUserWithEmailAndPassword,
  GoogleAuthProvider,
  signInWithPopup,
} from "firebase/auth";

const Sign_Up = () => {
  const provider = new GoogleAuthProvider();
  provider.addScope("https://www.googleapis.com/auth/contacts.readonly");

  const [email, setEmail] = useState(null);
  const [password, setPassword] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [IsError, setIsError] = useState(false);
  const [userId, setUserId] = useState(null);
  const handleSubmit = () => {
    const auth = getAuth();
    setLoading(true);
    setTimeout(
      createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
          const user = userCredential.user;
          setUserId(user.reloadUserInfo.localId);
        })
        .catch((error) => {
          const errorCode = error.code;
          const errorMessage = error.message;
          setIsError(true);
          setError(`${errorCode} ${errorMessage}`);
          setLoading(false);
        }),
      10000
    );
    setLoading(false);
  };
  const googleauth = () => {
    const auth = getAuth();
    signInWithPopup(auth, provider)
      .then((result) => {
        const credential = GoogleAuthProvider.credentialFromResult(result);
        const token = credential.accessToken;
        const user = result.user;
        console.log(user);
      })
      .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        const email = error.email;
        const credential = GoogleAuthProvider.credentialFromError(error);
      });
  };
  return (
    <>
      <div className="container">
        <div className="moto">Sign Up</div>
        <p>Create a new account to continue</p>
        <form>
          <FormControl fullWidth sx={{ m: 1 }}>
            <InputLabel htmlFor="outlined-adornment-amount">
              <h5>Email</h5>
            </InputLabel>
            <OutlinedInput
              id="outlined-adornment-amount"
              onChange={(e) => {
                setEmail(e.target.value);
              }}
              label="Email"
              value={email}
              placeholder="Email"
            />
          </FormControl>
          <FormControl fullWidth sx={{ m: 1 }}>
            <InputLabel htmlFor="outlined-adornment-amount">
              <h5>Password</h5>
            </InputLabel>
            <OutlinedInput
              id="outlined-adornment-amount"
              onChange={(e) => {
                setPassword(e.target.value);
              }}
              label="Password"
              type="password"
              value={password}
              placeholder="Password"
            />
          </FormControl>
          {!loading && (
            <FormControl sx={{ m: 1 }}>
              <Button variant="contained" onClick={handleSubmit}>
                Send
              </Button>
            </FormControl>
          )}
          {loading && (
            <FormControl sx={{ m: 1 }}>
              <div className="spinner-border" role="status">
                <span className="visually-hidden">Loading...</span>
              </div>
            </FormControl>
          )}
          {IsError && <p>{error}</p>}
        </form>
        <br />
        <button onClick={googleauth}>Login with Google</button>
      </div>
    </>
  );
};

export default Sign_Up;
