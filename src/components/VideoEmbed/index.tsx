import type {ReactNode} from 'react';
import styles from './styles.module.css';

type VideoEmbedProps = {
  videoId: string;
  title: string;
};

export default function VideoEmbed({videoId, title}: VideoEmbedProps): ReactNode {
  return (
    <div className={styles.videoWrapper}>
      <iframe
        className={styles.video}
        src={`https://www.youtube-nocookie.com/embed/${videoId}`}
        title={title}
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowFullScreen
      />
      <p className={styles.caption}>{title}</p>
    </div>
  );
}
