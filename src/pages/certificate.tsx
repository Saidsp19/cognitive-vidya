import {useState, useEffect, useCallback} from 'react';
import type {ReactNode} from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import Heading from '@theme/Heading';
import {
  PYTHON_LESSONS,
  DSA_LESSONS,
  QUIZ_KEYS,
  ALL_LESSON_IDS,
} from '@site/src/data/courseLessons';
import styles from './certificate.module.css';

function getProgress(): string[] {
  if (typeof window === 'undefined') return [];
  return JSON.parse(localStorage.getItem('cv-lesson-progress') || '[]');
}

function getQuizResults(): Record<string, {passed: boolean}> {
  if (typeof window === 'undefined') return {};
  return JSON.parse(localStorage.getItem('cv-quiz-results') || '{}');
}

export default function CertificatePage(): ReactNode {
  const [completed, setCompleted] = useState<string[]>([]);
  const [quizzes, setQuizzes] = useState<Record<string, {passed: boolean}>>({});
  const [name, setName] = useState('');
  const [showCert, setShowCert] = useState(false);

  const refresh = useCallback(() => {
    setCompleted(getProgress());
    setQuizzes(getQuizResults());
    setName(localStorage.getItem('cv-learner-name') || '');
  }, []);

  useEffect(() => {
    refresh();
    window.addEventListener('cv-progress-update', refresh);
    return () => window.removeEventListener('cv-progress-update', refresh);
  }, [refresh]);

  const lessonPct = Math.round((completed.length / ALL_LESSON_IDS.length) * 100);
  const quizzesPassed = QUIZ_KEYS.filter((k) => quizzes[k]?.passed).length;
  const quizPct = Math.round((quizzesPassed / QUIZ_KEYS.length) * 100);
  const overallPct = Math.round((lessonPct + quizPct) / 2);
  const eligible = overallPct >= 80 && quizzesPassed >= 7;

  const saveName = () => {
    localStorage.setItem('cv-learner-name', name);
  };

  const handlePrint = () => {
    window.print();
  };

  return (
    <Layout title="Certificate" description="Track your progress and earn your Cognitive Vidya certificate">
      <main className={styles.page}>
        <div className="container">
          <Heading as="h1">Your Progress & Certificate</Heading>
          <p className={styles.subtitle}>
            Mark lessons complete as you go, pass module quizzes, and earn your certificate at 80%+ overall progress.
          </p>

          <div className={styles.stats}>
            <div className={styles.statCard}>
              <span className={styles.statValue}>{lessonPct}%</span>
              <span className={styles.statLabel}>Lessons ({completed.length}/{ALL_LESSON_IDS.length})</span>
            </div>
            <div className={styles.statCard}>
              <span className={styles.statValue}>{quizPct}%</span>
              <span className={styles.statLabel}>Quizzes ({quizzesPassed}/{QUIZ_KEYS.length})</span>
            </div>
            <div className={styles.statCard}>
              <span className={styles.statValue}>{overallPct}%</span>
              <span className={styles.statLabel}>Overall</span>
            </div>
          </div>

          <div className={styles.progressBar}>
            <div className={styles.progressFill} style={{width: `${overallPct}%`}} />
          </div>

          <section className={styles.section}>
            <Heading as="h2">Python Course</Heading>
            <ul className={styles.checklist}>
              {PYTHON_LESSONS.map((lesson) => (
                <li key={lesson.id} className={completed.includes(lesson.id) ? styles.done : ''}>
                  {completed.includes(lesson.id) ? '✅' : '⬜'}{' '}
                  <Link to={`/docs/${lesson.id}`}>{lesson.title}</Link>
                  <span className={styles.moduleTag}>{lesson.module}</span>
                </li>
              ))}
            </ul>
          </section>

          <section className={styles.section}>
            <Heading as="h2">DSA Patterns</Heading>
            <ul className={styles.checklist}>
              {DSA_LESSONS.map((lesson) => (
                <li key={lesson.id} className={completed.includes(lesson.id) ? styles.done : ''}>
                  {completed.includes(lesson.id) ? '✅' : '⬜'}{' '}
                  <Link to={`/docs/${lesson.id}`}>{lesson.title}</Link>
                  <span className={styles.moduleTag}>{lesson.module}</span>
                </li>
              ))}
            </ul>
          </section>

          <section className={styles.section}>
            <Heading as="h2">Module Quizzes</Heading>
            <ul className={styles.checklist}>
              {QUIZ_KEYS.map((key) => (
                <li key={key} className={quizzes[key]?.passed ? styles.done : ''}>
                  {quizzes[key]?.passed ? '✅' : '⬜'}{' '}
                  <Link to={`/docs/python/quizzes/${key.replace('quiz-', '')}`}>
                    {key.replace('quiz-', '').replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase())}
                  </Link>
                </li>
              ))}
            </ul>
          </section>

          <section className={styles.certSection}>
            <Heading as="h2">Earn Your Certificate</Heading>
            {eligible ? (
              <div>
                <div className={styles.nameInput}>
                  <label htmlFor="learner-name">Your name (for certificate):</label>
                  <input
                    id="learner-name"
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    onBlur={saveName}
                    placeholder="Enter your full name"
                  />
                </div>
                <button type="button" className="button button--primary button--lg" onClick={() => setShowCert(true)}>
                  Generate Certificate
                </button>
                {showCert && name && (
                  <div className={styles.certificate}>
                    <div className={styles.certBorder}>
                      <p className={styles.certHeader}>Certificate of Completion</p>
                      <p className={styles.certAward}>This certifies that</p>
                      <p className={styles.certName}>{name}</p>
                      <p className={styles.certBody}>
                        has successfully completed the <strong>Cognitive Vidya</strong> Python Programming
                        course and DSA Patterns curriculum, demonstrating proficiency from beginner
                        to expert level.
                      </p>
                      <p className={styles.certDate}>
                        {new Date().toLocaleDateString('en-US', {year: 'numeric', month: 'long', day: 'numeric'})}
                      </p>
                      <p className={styles.certSig}>Cognitive Vidya · cognitive-vidya</p>
                    </div>
                    <button type="button" className="button button--secondary" onClick={handlePrint}>
                      Print / Save as PDF
                    </button>
                  </div>
                )}
              </div>
            ) : (
              <p className={styles.notEligible}>
                Complete at least <strong>80%</strong> overall progress and pass <strong>7 of 9</strong> quizzes to unlock your certificate.
                Current: {overallPct}% overall, {quizzesPassed}/9 quizzes passed.
              </p>
            )}
          </section>
        </div>
      </main>
    </Layout>
  );
}
