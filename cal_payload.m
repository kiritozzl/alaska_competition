path = '/home/zhouzl/alaska/payload/90/log1.txt'
input_path = '/home/zhouzl/alaska/payload/90/90_stego1_payload.txt'
jpg_path = '/data1/alaska/materials_qf/90/cover/ALASKA_training_set_JPG1/'
beta_payload = 0.3; % (qf-75)/150+0.2

text_file = fopen(path);
fid = fopen(input_path, 'a+');

while feof(text_file) ~= 1
	line = fgetl(text_file);
	s = regexp(line, '\s+', 'split');
	file_name = char(s(1));
	pay_load = str2num(char(s(6)));

	py = pay_load * (1-beta_payload);
	pcb = pay_load*beta_payload/2;
	
	jp = [jpg_path, file_name, '.jpg'];
	
	coeffs = jpeg_read(jp);
	c_coeffs = getfield(coeffs, 'coef_arrays');

	py_coeff = c_coeffs{1,1};
	py_nzAC = nnz(py_coeff)-nnz(py_coeff(1:8:end,1:8:end));
	py_payload = py/py_nzAC;
	
	pcb_coeff = c_coeffs{1,2};
	pcb_nzAC = nnz(pcb_coeff)-nnz(pcb_coeff(1:8:end,1:8:end));
	pcb_payload = pcb/pcb_nzAC;
	
	pcr_coeff = c_coeffs{1,3};
	pcr_nzAC = nnz(pcr_coeff)-nnz(pcr_coeff(1:8:end,1:8:end));
	pcr_payload = pcb/pcr_nzAC;
	
	
	fprintf(fid,'%s, py_payload %s, pcb_payload %s, pcr_payload %s,\n',file_name, py_payload, pcb_payload, pcr_payload);
	end
	
fclose(text_file);
fclose(fid);