// eslint-disable-next-line @typescript-eslint/no-unused-vars
import './app.module.scss';
import { HomeView } from './home-view/home-view';
import { StateContextProvider } from './fetch-context/fetch-context';

export function App() {
  return (
    <StateContextProvider>
      <HomeView />
    </StateContextProvider>
  );
}

export default App;
