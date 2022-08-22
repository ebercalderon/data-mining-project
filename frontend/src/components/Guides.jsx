import React from 'react';
import { NavLink } from "react-router-dom";
import { BsArrowRight } from "react-icons/bs";

const Guides = () => {

    return (
        <div className="bg-white dark:bg-slate-800">
            <section className='container mx-auto pb-20 lg:px-10'>
                <h1 className='text-5xl font-bold text-center mb-10 text-violet-800 px-2 dark:text-violet-400'>Installation Guides</h1>
                <div className='grid grid-rows-1 sm:grid-cols-3 my-5 mx-5 bg-slate-100 rounded-md shadow-md py-6 dark:bg-slate-700'>
                    <div className='col-span-2 px-4 sm:px-8'>
                        <h1 className='text-2xl font-bold text-violet-800 my-2 dark:text-violet-400'>Frontend</h1>
                        <div className='text-slate-500 dark:text-slate-200'>
                            In order to run this project locally, simply fork and clone the repository or download as zip and unzip on your machine.
                            <ul>- Open the project in your prefered code editor.</ul>
                            <ul>- Go to terminal -&gt; New terminal (If you are using VS code)</ul>
                            <ul>───────────────</ul>
                            In the terminal:
                        </div>
                        <div className='grid grid-rows-1 sm:grid-cols-1 my-5 bg-slate-300 rounded-md shadow-md py-6 dark:bg-slate-800'>
                            <div className='col-span-2 px-4 sm:px-8 notranslate text-slate-500 dark:text-slate-200'>
                                <div>
                                    <ul>$ cd ./frontend</ul>
                                    <ul>$ npm install</ul>
                                    <ul>$ npm start</ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className='col-span-2 sm:col-span-1 ps-22 sm:pr-8 flex justify-center sm:justify-end items-center'>
                        <a href="https://github.com/ebercalderon/data-mining-project" target="_blank">
                            <button className='rounded-3xl bg-teal-600 text-white font-semibold py-2 px-6 hover:bg-slate-700 dark:hover:bg-slate-800 hover:text-white duration-300 inline-flex items-center justify-center'>
                                Read More <BsArrowRight className='ml-1' />
                            </button>
                        </a>
                    </div>
                </div>
                <div className='grid grid-rows-1 sm:grid-cols-3 my-5 mx-5 bg-slate-100 rounded-md shadow-md py-6 dark:bg-slate-700'>
                    <div className='col-span-2 px-4 sm:px-8'>
                        <h1 className='text-2xl font-bold text-violet-800 my-2 dark:text-violet-400'>Backend</h1>
                        <div className='text-slate-500 dark:text-slate-200'>
                            Validate prerequisites.
                            <ul>In the terminal:</ul>
                        </div>
                        <div className='grid grid-rows-1 sm:grid-cols-1 my-5 bg-slate-300 rounded-md shadow-md py-6 dark:bg-slate-800'>
                            <div className='col-span-2 px-4 sm:px-8'>
                                <div className='notranslate text-slate-500 dark:text-slate-200'>
                                    <ul>$ cd ./backend</ul>
                                    <ul>$ python run.py</ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className='col-span-2 sm:col-span-1 ps-22 sm:pr-8 flex justify-center sm:justify-end items-center'>
                        <a href="https://github.com/ebercalderon/data-mining-project" target="_blank">
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

export default Guides;