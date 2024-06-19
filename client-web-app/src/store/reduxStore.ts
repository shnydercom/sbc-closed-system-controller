import { Action, combineSlices, configureStore, ConfigureStoreOptions, ThunkAction } from '@reduxjs/toolkit'
import { rtkQueryClientApi } from './rtkQueryClientApi'

// `combineSlices` automatically combines the reducers using
// their `reducerPath`s, therefore we no longer need to call `combineReducers`.
const rootReducer = combineSlices(rtkQueryClientApi)
// Infer the `RootState` type from the root reducer
export type RootState = ReturnType<typeof rootReducer>

export const createStore = (
	options?: ConfigureStoreOptions['preloadedState'] | undefined,
) =>
	configureStore({
		reducer: rootReducer,
		middleware: (getDefaultMiddleware) =>
			getDefaultMiddleware().concat(rtkQueryClientApi.middleware),
		...options,
	})

export const store = createStore()

export type AppDispatch = typeof store.dispatch
export type AppThunk<ThunkReturnType = void> = ThunkAction<
	ThunkReturnType,
	RootState,
	unknown,
	Action
>