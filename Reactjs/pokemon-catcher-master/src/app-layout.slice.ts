import { createSlice, PayloadAction } from "@reduxjs/toolkit";

export interface AppLayoutState {
  title: String,
  hasMenu: Boolean
}

const initialState: AppLayoutState = {
  title: '',
  hasMenu: true
}

const slice = createSlice({
  name: 'applayout',
  initialState,
  reducers: {
    setTitle: (state, action: PayloadAction<String>) => {
      state.title = action.payload
    },
    setHasMenu: (state, action: PayloadAction<Boolean>) => {
      state.hasMenu = action.payload
    }
  }
})

export const { setTitle, setHasMenu } = slice.actions

export default slice.reducer

