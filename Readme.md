This is a [Sublime Text][sublime] package containing frequently used snippets for [Cotonti CMF][cotonti] developers.

## List of snippets ##

 * cotajax - generates an AJAX part of an extension;
 * cotass - a snippet for template tags assignment;
 * cotcheck - a snippet for input validation via cot_check();
 * cotconf - inserts a new config line in an extension setup-file;
 * cotdbcol - fetches a single column value from the database;
 * cotdbdel - deletes matched rows from database;
 * cotdbins - inserts rows into a database table;
 * cotdbname - global table name declaration for variables like `$db_table_name`;
 * cotdbsel - common snippet for SELECTing data from the database;
 * cotdbupd - updates data in a database table;
 * cotforall - common snippet for fetching data from the database and rendering the rows in the template;
 * cothook - inserts a hook;
 * cotimp - a snippet for cot_import() function call;
 * cotimppagenav - imports pagination parameters;
 * cotlang - generates a lang-file;
 * cotnewxt - inserts construction of new XTemplate objects;
 * cotpagenav - generates pagination code with template assignment;
 * cotparse - inserts `$t->parse()` call;
 * cotplug - generates a hook-part of a plugin/module;
 * cotplugtpl - generates a hook-part which assigns some tpl tags;
 * cotreq - inserts `require_once cot_incfile()` statement;
 * cotset - generates a setup-file;
 * cotsqlcreate - inserts a CREATE TABLE statement with common properties;
 * cottool - a skeleton of an admin tool part of a plugin;
 * cottooltpl - a skeleton of a template for the admin tool part of a plugin;
 * cottpl - generates MAIN block of a TPL file;
 * cottplblock - inserts a block into a TPL file;
 * cottplcbk - inserts a CoTemplate callback tag;
 * cottplfile - inserts CoTemplate FILE statement;
 * cottplfor - inserts CoTemplate FOR statement;
 * cottplif - inserts CoTemplate IF statement;
 * cottplifels - inserts CoTemplate IF ... ELSE statement;

## Hotkeys ##

Select a line containing a Cotonti API funcion call starting with `cot_` prefix, e.g. `cot_input(...` and then hit "Ctrl + Alt + C" to open Cotonti Reference entry for that function.


## Installation ##

### With Package Control ###

If you have the [Package Control][package_control] package installed, you can install Cotonti Snippets from inside Sublime Text itself. Open the Command Palette and select "Package Control: Add Repository", then input this repository url. Reopen the Command Palette and select "Package Control: Install Package", then search for Cotonti.

### Without Package Control ###

If you haven't got Package Control installed (seriously, go install it!) you will need to make a clone of this repository into your packages folder, like so:

    git clone https://github.com/Cotonti/sublime-cotonti.git Cotonti


[sublime]: http://www.sublimetext.com/
[package_control]: http://wbond.net/sublime_packages/package_control
[cotonti]: http://www.cotonti.com
