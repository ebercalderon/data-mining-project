import React from 'react';
import Colab from '../images/colab.png'
import { BsArrowRight } from "react-icons/bs";

const Details = () => {

    return (
        <div className="bg-white dark:bg-slate-800">
            <section className='container mx-auto pb-20 lg:px-10'>
                <h1 className='text-5xl font-bold text-center mb-10 text-violet-800 px-2 pt-10 dark:text-violet-400'>Data Mining Project</h1>
                <div className='my-5 mx-5 bg-slate-100 rounded-md shadow-md py-6 dark:bg-slate-700'>
                    <div className='px-4 sm:px-8'>
                        <h1 className='text-2xl font-bold text-violet-800 my-2 dark:text-violet-400'>Problem Statement</h1>
                        <div className='text-slate-500 dark:text-slate-200'>
                            There has been a revenue decline for the Portuguese bank and they would like to know what actions to take.
                            After investigation, we found out that the root cause is that their clients are not depositing as frequently as before.
                            Knowing that term deposits allow banks to hold onto a deposit for a specific amount of time, so banks can invest in higher
                            gain financial products to make a profit. In addition, banks also hold better chance to persuade term deposit clients into
                            buying other products such as funds or insurance to further increase their revenues. As a result, the Portuguese bank would
                            like to identify existing clients that have higher chance to subscribe for a term deposit and focus marketing effort on such
                            clients.
                        </div>
                        <div className='my-5 bg-slate-300 rounded-md shadow-md py-6 dark:bg-slate-800'>
                            <div className='px-4 sm:px-8 text-slate-500 dark:text-slate-200'>
                                <h1 className='text-2xl font-bold text-slate-500 my-2 dark:text-slate-200'>About the Dataset</h1>
                                <h3> Source of the data:
                                    <a href="https://archive.ics.uci.edu/ml/datasets/bank+marketing" target="_blank" rel="noreferrer"> <u>https://archive.ics.uci.edu/ml/datasets/bank+marketing</u></a>
                                </h3>
                                <iframe className='h-64 py-5' src="https://www.kaggle.com/embed/benroshan/bank-marketing-campaign-predictive-analytics?kernelSessionId=39196738" width="100%" height="100%" title="Bank marketing campaign | Predictive analytics"></iframe>
                            </div>
                        </div>
                    </div>
                    <div className='ps-22 sm:pr-8 flex justify-center sm:justify-end items-center'>
                        <a href="https://www.kaggle.com/code/benroshan/bank-marketing-campaign-predictive-analytics?kernelSessionId=39196738" target="_blank" rel="noreferrer">
                            <button className='rounded-3xl bg-teal-600 text-white font-semibold py-2 px-6 hover:bg-slate-700 dark:hover:bg-slate-800 hover:text-white duration-300 inline-flex items-center justify-center'>
                                Read More <BsArrowRight className='ml-1' />
                            </button>
                        </a>
                    </div>
                </div>
            </section>
            <section className='container mx-auto pb-20 lg:px-10'>
                <h1 className='text-5xl font-bold text-center mb-10 text-violet-800 px-2 dark:text-violet-400'>Colab Project</h1>
                <div className='my-5 mx-5 bg-slate-100 rounded-md shadow-md py-6 dark:bg-slate-700'>
                    <div className='px-4 sm:px-8'>
                        <h1 className='text-2xl font-bold text-violet-800 my-2 dark:text-violet-400'>Random forest</h1>
                        <div className='text-slate-500 dark:text-slate-200'>
                            Random forest is a flexible, easy-to-use machine learning algorithm that produces, even without hyper-parameter tuning, a great result most of the time. 
                            It is also one of the most-used algorithms, due to its simplicity and diversity (it can be used for both classification and regression tasks).
                        </div>
                        <div className='my-5 bg-slate-300 rounded-md shadow-md py-6 dark:bg-slate-800'>
                            <div className='px-4 sm:px-8 text-slate-500 dark:text-slate-200'>
                                <h1 className='text-2xl font-bold text-slate-500 my-2 dark:text-slate-200'>About the Dataset</h1>
                                <h3> Source of the data:
                                    <a href="https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html" target="_blank" rel="noreferrer"> <u>sklearn.datasets.load_breast_cancer</u></a>
                                </h3>
                                <img src={Colab} width="100%" height="100%" alt="/" className='py-5'></img>
                            </div>
                        </div>
                    </div>
                    <div className='ps-22 sm:pr-8 flex justify-center sm:justify-end items-center'>
                        <a href="https://colab.research.google.com/drive/1Pp9Il01kb8mimM2s-6PXjN2U36TnxG_n?usp=sharing" target="_blank" rel="noreferrer">
                            <button className='rounded-3xl bg-teal-600 text-white font-semibold py-2 px-6 hover:bg-slate-700 dark:hover:bg-slate-800 hover:text-white duration-300 inline-flex items-center justify-center'>
                                Read More <BsArrowRight className='ml-1' />
                            </button>
                        </a>
                    </div>
                </div>
            </section>
        </div>
    );
};

export default Details;