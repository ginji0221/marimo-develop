import marimo

__generated_with = "0.15.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import os
    import glob
    import pandas as pd
    return glob, mo, os, pd


@app.cell
def _(mo):
    def exec_sql(query):
        """
        SQLを実行する関数

        Args:
            query (str): SQLクエリ
        Returns:
            result (object): 実行結果 (テーブル情報 or エラー情報)
        """
        try:
            result = mo.sql(query)
            return result
        except Exception as e:
            result = mo.md(f"**エラー:**\n\n```\n{e}\n```")
            return result
    return (exec_sql,)


@app.cell
def _(glob, mo, os, pd):
    # CSVファイルをSQLテーブルとして登録
    files = {}
    file_paths = glob.glob('tables/*.csv')
    for file_path in file_paths:
        # ファイルパスを変数に代入
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        df_table = pd.read_csv(file_path)
        globals()[file_name] = df_table

        # ファイル情報の登録
        files[file_name] = mo.ui.table(data=df_table, pagination=True, page_size=5)

    # UIコンポーネントの作成
    initial_code = ""
    sql_input_component = mo.ui.code_editor(value=initial_code, language="sql")
    run_btn = mo.ui.run_button(label="RUN")
    save_btn = mo.ui.run_button(label="SAVE")
    table_list_component = mo.vstack(
        [
            mo.md("## Tables"),
            mo.accordion(files, multiple=True),
        ],
        gap=1,
        align="stretch",
    )

    # 実行結果を保持
    get_result, set_result = mo.state(mo.md('write sql query and push "RUN" button.'))
    return (
        get_result,
        run_btn,
        save_btn,
        set_result,
        sql_input_component,
        table_list_component,
    )


@app.cell
def _(
    exec_sql,
    get_result,
    mo,
    run_btn,
    save_btn,
    set_result,
    sql_input_component,
    table_list_component,
):
    # run_btnの値を参照してロジックを実行
    if run_btn.value:
        set_result(exec_sql(query=sql_input_component.value))

    # UIコンポーネントをレイアウト
    btn_component = mo.hstack(
        [run_btn, save_btn],
        justify="end",
        gap=1,
    )

    sql_form_component = mo.vstack(
        [
            mo.md("## Query"),
            sql_input_component, 
            btn_component
        ],
        align="stretch",
        gap=1,
    )

    result_component = mo.vstack(
        [
            mo.md("## Result"),
            get_result(),
        ],
        align="stretch",
        gap=1,
    )

    editor_component = mo.vstack(
        [sql_form_component, result_component],
        gap=3,
        align="stretch",
        heights=[1, 1]
    )

    main_component = mo.vstack(
        [
            mo.center(mo.md("# SQL Playground")),
            mo.hstack(
                [editor_component, table_list_component],
                gap=3,
                align="stretch",
                widths=[1, 1]
            ),
        ],
        gap=3,
        align="stretch",
    )

    # 最終的なコンポーネントを表示
    main_component
    return


if __name__ == "__main__":
    app.run()
