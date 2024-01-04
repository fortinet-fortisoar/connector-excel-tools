
<h2>About the connector</h2>

<p>Utility to manage excel files</p>

<p>This document provides information about the Excel Tools Connector, which facilitates automated interactions, with a Excel Tools server using FortiSOAR&trade; playbooks. Add the Excel Tools Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Excel Tools.</p>

<h3>Version information</h3>

<p>Connector Version: 1.0.0</p>

<p>Authored By: Fortinet CSE</p>

<p>Contributors: Naili Mahdi</p>

<p>Certified: No</p>

<h2>Installing the connector</h2>

<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>

<pre>yum install cyops-connector-excel-tools</pre>

<h2>Prerequisites to configuring the connector</h2>

<p>There are no prerequisites to configuring this connector.</p>

<h2>Minimum Permissions Required</h2>

<ul>
<li>Not applicable</li>
</ul>

<h2>Configuring the connector</h2>

<p>For the procedure to configure a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector">here</a></p>

<h3>Configuration parameters</h3>

<p>None.</p>

<h2>Actions supported by the connector</h2>

<p>The following automated operations can be included in playbooks and you can also use the annotations to access operations:</p>

<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Read Sheet</td><td>Read the sheet content by name and return all content as JSON</td><td>read_sheet <br/></td></tr>
<tr><td>Read Column By Name</td><td>Read the column content by name</td><td>read_column_by_name <br/></td></tr>
<tr><td>Update Column</td><td>Update cells values in a column</td><td>update_column <br/></td></tr>
<tr><td>Update Cell</td><td>Update the value of a cell</td><td>update_cell <br/></td></tr>
<tr><td>List Sheets</td><td>Lists available sheets names</td><td>list_sheets <br/></td></tr>
</tbody></table>

<h3>operation: Read Sheet</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>File IRI</td><td>IRI of the excel file to read
</td></tr><tr><td>Sheet Name</td><td>Name of the sheet to read
</td></tr><tr><td>Use Column Title</td><td>Use the column title as a key for each cell value on that column instead of the cell coordinates. The sheet must have a title row on the top
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<p>The output contains a non-dictionary value.</p>

<h3>operation: Read Column By Name</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>File IRI</td><td>IRI of the excel file to edit
</td></tr><tr><td>Sheet Name</td><td>Name of the sheet to edit
</td></tr><tr><td>Column Name</td><td>Name of the column you want to read.
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<p>The output contains a non-dictionary value.</p>

<h3>operation: Update Column</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>File IRI</td><td>IRI of the excel file to edit
</td></tr><tr><td>Sheet Name</td><td>Name of the sheet to edit
</td></tr><tr><td>Select Column By</td><td>Select column by name or position
<br><strong>If you choose 'Name'</strong><ul><li>Cells Definitions: Cells definition JSON dictionary</li></ul><strong>If you choose 'Position'</strong><ul><li>Column Index: Index of the column to update</li><li>First Row Index: Index of the first row to update</li><li>Cells Values: CSV or list of the values to update the column with</li></ul></td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<p>The output contains a non-dictionary value.</p>

<h3>operation: Update Cell</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>File IRI</td><td>IRI of the excel file to edit
</td></tr><tr><td>Sheet Name</td><td>Name of the sheet to edit
</td></tr><tr><td>Cell ID</td><td>Cell to edit,exp: A1, B3...
</td></tr><tr><td>Value</td><td>Value to update the cell with
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<p>The output contains a non-dictionary value.</p>

<h3>operation: List Sheets</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>File IRI</td><td>IRI of the excel file
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<p>The output contains a non-dictionary value.</p>

<h2>Included playbooks</h2>

<p>The <code>Sample - excel-tools - 1.0.0</code> playbook collection comes bundled with the Excel Tools connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the <strong>Automation</strong> &gt; <strong>Playbooks</strong> section in FortiSOAR&trade; after importing the Excel Tools connector.</p>

<ul>
<li>List Sheet Names</li>
<li>Read Column By Name</li>
<li>Read Sheet</li>
<li>Update Cell</li>
<li>Update Column</li>
</ul>

<p><strong>Note</strong>: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.</p>
