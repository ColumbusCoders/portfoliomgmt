#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 20:59:08 2023

@author: saravananveeramani
"""

import streamlit as st
import Dividends as lib


st.header("{}".format(st.session_state.ticker))
incomestmt,balancesheet,cashflow = st.tabs(['Income Statement','Balance Sheet','Cashflow'])


with incomestmt:
    st.header('Income Statememt')
    df=lib.getTicker(st.session_state.ticker ).incomestmt
    st.dataframe(df.style.highlight_max(axis=1))

with balancesheet:
    st.header('Balance sheet')
    df=lib.getTicker(st.session_state.ticker ).balancesheet
    st.dataframe(df.style.highlight_max(axis=1))
    
with cashflow:
    st.header('Cashflow')
    df=lib.getTicker(st.session_state.ticker ).cashflow
    st.dataframe(df.style.highlight_max(axis=1))    
