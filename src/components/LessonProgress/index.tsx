import {useState, useEffect, useCallback} from 'react';
import type {ReactNode} from 'react';
import styles from './styles.module.css';

const STORAGE_KEY = 'cv-lesson-progress';

type LessonProgressProps = {
  lessonId: string;
  label?: string;
};

export function isLessonComplete(lessonId: string): boolean {
  if (typeof window === 'undefined') return false;
  const stored = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]') as string[];
  return stored.includes(lessonId);
}

export function getCompletedCount(ids: string[]): number {
  if (typeof window === 'undefined') return 0;
  const stored = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]') as string[];
  return ids.filter((id) => stored.includes(id)).length;
}

export default function LessonProgress({lessonId, label = 'Mark lesson complete'}: LessonProgressProps): ReactNode {
  const [complete, setComplete] = useState(false);

  useEffect(() => {
    setComplete(isLessonComplete(lessonId));
  }, [lessonId]);

  const toggle = useCallback(() => {
    const stored = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]') as string[];
    const next = complete
      ? stored.filter((id) => id !== lessonId)
      : [...stored, lessonId];
    localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
    setComplete(!complete);
    window.dispatchEvent(new Event('cv-progress-update'));
  }, [complete, lessonId]);

  return (
    <button
      type="button"
      className={complete ? styles.complete : styles.incomplete}
      onClick={toggle}>
      {complete ? '✅ Lesson completed' : `⬜ ${label}`}
    </button>
  );
}
