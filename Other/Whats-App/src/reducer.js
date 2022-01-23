/*
sumary_line

Keyword arguments:
argument -- description
Return: return_description
*/
export const initialState = {
  user: null,
};
export const actionTypes = {
  SET_USER: "SET_USER",
};
const reducer = (state, action) => {
  console.log(action);
  console.log("State ", state);
  switch (action.type) {
    case actionTypes.SET_USER:
      return {
        ...state,
        user: action.user,
      };
    default:
      return state;
  }
};

export default reducer;
