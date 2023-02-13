import styles from './home-view.module.scss';

/* eslint-disable-next-line */
export interface HomeViewProps {}

export function HomeView(props: HomeViewProps) {
  return (
    <div className={styles['container']}>
      <h1>Welcome to HomeView!</h1>
    </div>
  );
}

export default HomeView;
